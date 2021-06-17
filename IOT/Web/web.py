import time
import sys
sys.path.insert(1, '/home/test/XMPP/')
from XMPP_API import XMPP_Offline
import json
import threading

message_recu = list()


def actualisation(msg):
    global message_recu
    ts = int(time.time())

    for donnee in message_recu[:]:
        if donnee["id_evt"] == msg["id_evt"] and donnee["cause_code"] == msg["cause_code"]:
            message_recu.remove(donnee)
        if donnee in message_recu and ts - donnee["time"] > 300:
            message_recu = message_recu[message_recu.index(donnee) + 1:]
            break

    message_recu.insert(0, msg)



def ecriture(donnees):
    f = open('events.json', 'w+')
    f.write(json.dumps(donnees))
    f.close()


def gestion_web():
    global server
    while True:
        consumme = server.getLastMessage()
        if consumme != None :
            sender = consumme[1]
            msg = consumme[0]
            if sender == "evt@valouzze.local":
                print("sender : " + str(sender) + " msg: " + str(msg))
                print('\n')
                actualisation(json.loads(msg))
                ecriture(message_recu)


server = XMPP_Offline("web", "valouzze.local", "test")

receive = threading.Thread(target=server.receive_message)
receive.start()

time.sleep(1)
print("ok")

sending = threading.Thread(target=gestion_web())
sending.start()