import sys
sys.path.insert(1, '/home/test/XMPP/')
from XMPP_API import XMPP_Offline

#Vérification que l'on reçoit bien les messages

receiver = XMPP_Offline("admin", "valouzze.local", "test")
receiver.receive_message()

#Vérification que l'on reçoit bien les messages sur un autre client
#Si on veut plusieurs client en même temps il faudra utiliser des threads

new_receiver = XMPP_Offline("admin", "localhost", "test")
new_receiver.receive_message()

#Essayons de recevoir sur un client non existant pour la gestion d'erreur

false_receiver = XMPP_Offline("machin", "valouzze.local", "truc")
false_receiver.receive_message()