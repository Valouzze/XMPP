import sys
sys.path.insert(1, '/home/test/XMPP/')
from XMPP_API import XMPP_Offline

#Envoie d'un utilisateur à un autre sur le même domaine

sender = XMPP_Offline("test", "valouzze.local", "test")
sender.send_message("Hello world ! :)", "admin", "valouzze.local")

#Envoie d'un utilisateur à un autre sur des domaines différents

sender.send_message("Hello world ! :)", "admin", "localhost")

#Tentative de connexion sur un utilisateur n'existant pas et d'envoie de message

new_sender = XMPP_Offline("machin", "valouzze.local", "truc")
new_sender.send_message("Hello world :)" ,"admin", "valouzze.local")