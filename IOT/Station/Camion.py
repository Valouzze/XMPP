import sys
sys.path.insert(1, '/home/test/XMPP/')
from XMPP_API import XMPP_Offline
import random
import time

class Camion:
    def __init__(self, station_id, station_type, vitesse, x, y, direction, username, domain, password):
        self.station_id = station_id
        self.station_type = station_type
        self.vitesse = vitesse
        self.pos = [0,0]
        self.direction = direction

        self.client = XMPP_Offline(username, domain, password)



    def set_direction(self, direction):
        self.direction = direction

    def deplacement(self):
        self.pos[0] += self.direction[0] * (self.vitesse / 10)
        self.pos[1] += self.direction[1] * (self.vitesse / 10)
        self.vitesse += random.randint(-10, 10)
        if self.vitesse < 1:
            self.vitesse = 10

    def envoie_message(self):
        ts = int(time.time())
        message = '{"station_id":' + str(self.station_id) + ', "station_type":' + str(
            self.station_type) + ', "vitesse":' + str(self.vitesse) + ', "pos_x":' + str(
            self.pos[0]) + ', "pos_y": ' + str(self.pos[1]) + ', "time":' + str(ts) + '}'

        #time.sleep(0.1)

        if random.randint(0, 100) <= 100:
            self.client.send_message(message, "passerelle", "valouzze.local")

    def envoie_evenement(self, cause_code, subcause_code):

        ts = int(time.time())
        message = '{"station_id":' + str(self.station_id) + ', "station_type":' + str(
            self.station_type) + ', "cause_code":' + str(cause_code) + ', "pos_x":' + str(
            self.pos[0]) + ', "pos_y": ' + str(self.pos[1]) + ', "subcause_code":' + str(subcause_code) + ', "time":' + str(ts) + '}'

        #time.sleep(0.1)

        if random.randint(0, 100) <= 100:
            self.client.send_message(message, "passerelle", "valouzze.local")


    def lancement(self):
        while True:
            time.sleep(0.1)
            self.deplacement()
            if self.vitesse > 90:
                time.sleep(0.01)
                self.envoie_message()
            else:
                time.sleep(0.1)
                self.envoie_message()
            if random.randint(0, 100) <= 0:
                self.envoie_evenement(4,5)

c1 = Camion(9, 10, 20, 1 , 1, 10, "station", "valouzze.local", "test")
c2 = Camion(2, 10, 15, 1 , 1, 10, "station", "valouzze.local", "test")
c3 = Camion(1, 10, 18, 1 , 1, 10, "station", "valouzze.local", "test")
c1.envoie_message()
c2.envoie_message()
c3.envoie_message()