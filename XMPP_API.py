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
        self.lastMessage = list()

    def send_message(self, msg, receiver_username, receiver_domain):
        '''
        Envoie un message privé à l'utilisateur choisi et de son nom de domaine
        '''
        client = xmpp.protocol.JID(self.jid)
        cl=xmpp.Client(client.getDomain(),debug=[])
        if cl.connect() == "":
            print("Non connecté")
            sys.exit(0)

        if cl.auth(client.getNode(),self.passw) == None:
            print("Problème d'authentification")
            sys.exit(0)
        else:
            receiver_jid = receiver_username + '@' + receiver_domain
            print(self.jid)
            cl.send(xmpp.protocol.Message(receiver_jid,msg))
            cl.disconnect()
            return 1

    #Définition de fonctions servant à faire un affichage propre lors de réception de messages
    #avec gestions d'erreurs, on continue à recevoir des messages tant que le processus
    #de réception de message n'est pas coupé

    def messageCB(self,conn,msg):
        '''
        Fonction annexe utilisée pour receive_message
        '''
        print("Sender: " + str(msg.getFrom()))
        print("Content: " + str(msg.getBody()))
        print('\n')
        self.lastMessage.append([str(msg.getBody()), str(msg.getFrom()).rsplit('/', 1)[0] ])


    def StepOn(self,conn):
        '''
        Fonction annexe utilisée pour receive_message
        '''
        try:
                conn.Process(1)
        except KeyboardInterrupt:
                return 0
        return 1

    def GoOn(self,conn):
        '''
        Fonction annexe utilisée pour receive_message
        '''
        while self.StepOn(conn):
                pass

    def receive_message(self):
        '''
        Fonction permettant de mettre en mode écoute le client XMPP pour ses messages privés hors ligne, en les affichants sur le terminal
        '''
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
    
    def getLastMessage(self):
        '''
        Retourne le dernier message du client et le consumme
        '''
        length = len(self.lastMessage)
        if length == 0 :
            return None
        else:
            to_return = self.lastMessage[0]
            self.lastMessage.pop(0)
            return to_return

class XMPP_MUC:
    "Définition d'un client XMPP ayant accès à un MUC"
    def __init__(self, username, domain, password):
        self.passw = password
        self.user = username
        self.domain = domain
        self.jid = username + '@' + domain
        self.lastMessage = list()

    def send_muc(self, message, muc_room):
        '''
        Fonction permettant d'envoyer un message à un groupe d'utilisateurs (MUC)
        '''
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
        '''
        Fonction annexe utilisée pour receive_muc
        '''
        if msg.getType() == "groupchat" and (msg.getBody != None):
                print(str(msg.getFrom()) +": "+  str(msg.getBody()))
                self.lastMessage.append([str(msg.getBody()), str(msg.getFrom()).rsplit('/', 1)[0] ])
        if msg.getType() == "chat":
                print("private: " + str(msg.getFrom()) +  ":" +str(msg.getBody()))
                self.lastMessage.append([str(msg.getBody()), str(msg.getFrom()).rsplit('/', 1)[0] ])

    def StepOn(self,conn):
        '''
        Fonction annexe utilisée pour receive_muc
        '''
        try:
            conn.Process(1)
        except KeyboardInterrupt:
                return 0
        return 1

    def GoOn(self,conn):
        '''
        Fonction annexe utilisée pour receive_muc
        '''
        while self.StepOn(conn):
            pass

#Permet de lire tout les messages sur le MUC, les messages avant execution qui sont donc
#contenus dans l'historique sont affichés avant le message None
#Et ceux reçu en cours d'execution après le None
    def receive_muc(self, muc_room):

        '''
        Cette fonction permet d'afficher tout l'historique de messages d'un groupe d'utilisateurs (MUC)
        Puis ensuite affiche un message "None" et laisse le client en mode écoute, ce qui lui permet de continuer
        à recevoir les messages qui pourraient être envoyé dans le MUC
        '''

        client=xmpp.protocol.JID(self.jid)

        cl = xmpp.Client(client.getDomain(), debug=[])

        if cl.connect() == "":
                print("not connected")
                sys.exit(0)

        if cl.auth(client.getNode(),self.passw) == None:
                print("authentication failed")
                sys.exit(0)


        cl.sendInitPresence()

        cl.RegisterHandler('message', self.messageCB)

        room = muc_room
        print("Joining " + room)

        cl.send(xmpp.Presence(to="%s %s" % (room + "/", self.jid)))

        self.GoOn(cl)

class Ejabberd_Server:
    '''
    Classe contenant des fonctions utiles à un serveur ejabberd
    /!\  Il faut que l'utilisateur de ces fonctions aient accès à ejabberdctl autrement cela donnera juste lieu à un
    "Permission denied"
    '''
    def register_user(name, domain, password):
        '''
        Enregistre un utilisateur en fournissant un nom, son domaine, et son mot de passe
        '''
        os.system("ejabberdctl register " + name + " " + domain  + " " + password)

    def remove_user(name, domain):
        '''
        Supprime un utilisateur en fournissant son nom et son domaine
        '''
        os.system("ejabberdctl unregister " + name + " " + domain)

    def list_of_user(domain):
        '''
        Affiche dans le terminal la liste de tout les utilisateurs d'un domaine
        '''
        os.system("ejabberdctl registered_users " + domain)

    def create_muc(name_room, service, domain):
        '''
        Création d'un groupe de chat d'utilisateurs (MUC) en fournissant un nom pour ce canal d'utilisation, un service, et le domaine
        '''
        os.system("ejabberdctl create_room "+ name_room + " " + service + " " + domain)

    def delete_muc(name_room, service):
        '''
        Suppression d'un MUC en fournissant le nom du canal, et son service
        '''
        os.system("ejabberdctl destroy_room "+ name_room + " " + service)