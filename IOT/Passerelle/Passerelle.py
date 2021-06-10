import sys
sys.path.insert(1, '/home/test/XMPP/')
from XMPP_API import XMPP_Offline
import json
import threading
import time

def gestion_accident():
    compteur_evt = 0
    temps = 0
    id = list()
    for message in vehicule:
        if "cause_code" in message and message["cause_code"] == 4 and message["station_id"] not in id and message["station_id"] != "NULL":
            if temps - message["time"] > 600:
                print("Delai depassé ou déjà traité")
                break
            if compteur_evt == 0:
                temps = message["time"]
                compteur_evt += 1
                id.append(message["station_id"])
            elif 600 > temps - message["time"] > -1:
                compteur_evt += 1
                id.append(message["station_id"])
            if compteur_evt > 1 or message["station_type"] == 15:
                id.sort()
                res = '{ "station_id":' + str(message["station_id"]) + ', "station_type":' + str(
                    message["station_type"]) + ', "cause_code":4, "time":' + str(message["time"]) + ', "id_evt":'+str(id)+'}'
                message["station_id"] = "NULL"
                client.send_message(str(res), "evt", "valouzze.local")
                break


def gestion_embouteillage():
    compteur_emb = 0
    temps = 0
    id = list()
    for message in vehicule:
        if "vitesse" in message and message["vitesse"] < 30 and message["station_id"] not in id and message["station_id"] != "NULL":
            if temps - message["time"] > 120:
                print("Delai depassé ou déjà traité")
                break
            if compteur_emb == 0:
                temps = message["time"]
                compteur_emb += 1
                id.append(message["station_id"])
            elif 120 > temps - message["time"] > -1:
                compteur_emb += 1
                id.append(message["station_id"])

        if compteur_emb > 2:
            id.sort()
            res = '{ "station_id":' + str(message["station_id"]) + ', "station_type":' + str(message["station_type"]) + ', "cause_code":5, "time":' + str(message["time"]) + ', "id_evt":'+str(id)+'}'
            message["station_id"] = "NULL"
            client.send_message(str(res), "evt", "valouzze.local")
            break

vehicule = list()
client = XMPP_Offline("passerelle", "valouzze.local", "test")


def gestion_send(vehicule):
    global client
    while True:
        consumme = client.getLastMessage()
        if consumme != None :
            sender = consumme[1]
            msg = consumme[0]
            print("sender : " + str(sender) + " msg: " + str(msg))
            print('\n')
            vehicule.insert(0, json.loads(msg))
            gestion_embouteillage()
            gestion_accident()


receive = threading.Thread(target=client.receive_message)
receive.start()

time.sleep(1)
print("ok")

sending = threading.Thread(target=gestion_send(vehicule))
sending.start()
