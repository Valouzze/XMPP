import sys
import xmpp
import os
import signal
import time

class XMPP_Offline:
    "Définition d'un client XMPP avec file de message en offline"
    def __init__(self, username, domain, password):
        self.passw = password
        self.user = username
        self.domain = domain
        self.jid = username + '@' + domain

    def send_message(self, msg, receiver_username, receiver_domain):
        client = xmpp.protocol.JID(self.jid)
        cl=xmpp.Client(client.getDomain(),debug=[])
        if cl.connect() == "":
            print("Non connecté")
            sys.exit(0)

        if cl.auth(client.getNode(),self.passw) == None:
            print("Problème d'authentification")
            sys.exit(0)
        #On vérifie pour envoyer un message que les deux sont dans le même domaine
        if receiver_domain != self.domain:
            print("Sender domain : " + self.domain + "\n Receiver domain : " + receiver_domain + '\n')
            print("L'envoyeur et le receveur ne sont pas dans le même domaine")
            return -1
        else:
            receiver_jid = receiver_username + '@' + receiver_domain
            cl.send(xmpp.protocol.Message(receiver_jid,msg))
            cl.disconnect()
            return 1

    #Définition de fonctions servant à faire un affichage propre lors de réception de messages
    #avec gestions d'erreurs, on continue à recevoir des messages tant que le processus
    #de réception de message n'est pas coupé

    def messageCB(self,conn,msg):
        print("Sender: " + str(msg.getFrom()))
        print("Content: " + str(msg.getBody()))
        print(msg)


    def StepOn(self,conn):
        try:
                conn.Process(1)
        except KeyboardInterrupt:
                return 0
        return 1

    def GoOn(self,conn):
        while self.StepOn(conn):
                pass

    def receive_message(self):
        client=xmpp.protocol.JID(self.jid)

        cl = xmpp.Client(client.getDomain(), debug=[])

        if cl.connect() == "":
                print("not connected")
                sys.exit(0)

        if cl.auth(client.getNode(),self.passw) == None:
                print("authentication failed")
                sys.exit(0)
        cl.RegisterHandler('message', self.messageCB)

        cl.sendInitPresence()

        self.GoOn(cl)

class XMPP_MUC:
    "Définition d'un client XMPP ayant accès à un MUC"
    def __init__(self, username, domain, password):
        self.passw = password
        self.user = username
        self.domain = domain
        self.jid = username + '@' + domain

    def send_muc(self, message, muc_room):
        client = xmpp.protocol.JID(self.jid)
        cl=xmpp.Client(client.getDomain(),debug=[])
        if cl.connect() == "":
            print("Non connecté")
            sys.exit(0)

        if cl.auth(client.getNode(),self.passw) == None:
            print("Problème d'authentification")
            sys.exit(0)
        
        cl.send(xmpp.Presence(to="%s%s" % (muc_room + "/", self.jid)))
        msg = xmpp.protocol.Message(body=message)
        msg.setTo(muc_room)
        msg.setType('groupchat')
        cl.send(msg)
        cl.disconnect()
        return 1

    def messageCB(self,conn,msg):
        if msg.getType() == "groupchat" and (msg.getBody != None):
                print(str(msg.getFrom()) +": "+  str(msg.getBody()))
                print(msg.getBody)
        if msg.getType() == "chat":
                print("private: " + str(msg.getFrom()) +  ":" +str(msg.getBody()))

    def StepOn(self,conn):
        try:
            conn.Process(1)
        except KeyboardInterrupt:
                return 0
        return 1

    def GoOn(self,conn):
        while self.StepOn(conn):
            pass

#Permet de lire tout les messages sur le MUC, les messages avant execution qui sont donc
#contenus dans l'historique sont affichés avant le message None
#Et ceux reçu en cours d'execution après le None
    def receive_muc(self, muc_room):

        client=xmpp.protocol.JID(self.jid)

        cl = xmpp.Client(client.getDomain(), debug=[])

        cl.connect()

        cl.auth(client.getNode(),self.passw)


        cl.sendInitPresence()

        cl.RegisterHandler('message', self.messageCB)

        room = muc_room
        print("Joining " + room)

        cl.send(xmpp.Presence(to="%s %s" % (room + "/", self.jid)))

        self.GoOn(cl)

#Ces fonctions de l'API ne fonctionne qu'avec un serveur ejabberd !
#Il faut également que l'utilisateur qui lance le script python soit root ou ejabberd
def register_user(name, domain, password):
    os.system("ejabberdctl register " + name + " " + domain  + " " + password)

#Attention avec cette fonction car elle ne retourne rien donc il n'y a aucune confirmation de suppression
def remove_user(name, domain):
    os.system("ejabberdctl unregister " + name + " " + domain)

#Liste tout les utilisateurs d'un domaine (dans le terminal pour le moment)
def list_of_user(domain):
    os.system("ejabberdctl registered_users " + domain)

#Crée un MUC
def create_muc(name_room, service, domain):
    os.system("ejabberdctl create_room "+ name_room + " " + service + " " + domain)

#Supprime un MUC existant
def delete_muc(name_room, service):
    os.system("ejabberdctl destroy_room "+ name_room + " " + service)