import sys
sys.path.insert(1, '/home/test/XMPP/')
from XMPP_API import XMPP_Offline
import json
import threading
import time
import psycopg2

HOST = "localhost"
USER = "postgres"
PASSWORD = "test"
DATABASE = "save"

conn = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST, DATABASE, USER, PASSWORD))
cur = conn.cursor()

server = XMPP_Offline("backup", "valouzze.local", "test")

def envoyer_requete(evt):
    res = json.loads(evt)
    sql = "INSERT INTO evenements (station_id, station_type, cause_code, time) VALUES (" + str(res["station_id"]) + "," + str(res[
        "station_type"]) + "," + str(res["cause_code"]) + "," + str(res["time"]) + ");"
    cur.execute(sql)
    conn.commit()

def gestion_consommation():
    global server
    while True:
        consumme = server.getLastMessage()
        if consumme != None:
            sender = consumme[1]
            msg = consumme[0]
            print("sender : " + str(sender) + " msg: " + str(msg))
            print('\n')
            if sender == "tampon@valouzze.local":
                envoyer_requete(msg)
                print("Nouvelle donnée envoyée à la BDD \n")


receive = threading.Thread(target=server.receive_message)
receive.start()

time.sleep(1)
print("ok")

sending = threading.Thread(target=gestion_consommation)
sending.start()