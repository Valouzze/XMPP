import sys
sys.path.insert(1, '/home/test/XMPP/')
from XMPP_API import XMPP_MUC
import time

#Envoi d'un message avec un utilisateur d'un serveur A

sender = XMPP_MUC("admin", "valouzze.local", "test")
sender.send_muc("Hey everyone !", "chat_room@conference.valouzze.local")

#Ici nous allons faire une pause car il est impossible de voir sur l'interface
#web les messages sur le MUC mais seulement le timer du  dernier message
#afin de pouvoir produire 2 screenshots dans un temps espacés

time.sleep(20)

new_sender = XMPP_MUC("test", "localhost", "test")
new_sender.send_muc("Hey everyone !", "chat_room@conference.valouzze.local")

#Maintenant essayons avec un utilisateur non existant

false_sender = XMPP_MUC("machin", "valouzze.local", "truc")
false_sender.send_muc("Hey everyone !", "chat_room@conference.valouzze.local")
