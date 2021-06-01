import sys
import xmpp
import os
import signal
import time

class XMPP_Client:
    "Définition d'un client XMPP"
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

