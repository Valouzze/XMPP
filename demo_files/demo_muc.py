import sys
sys.path.insert(1, '/home/test/XMPP/')
from XMPP_API import XMPP_MUC

#Réception du client existant

receiver = XMPP_MUC("admin", "valouzze.local", "test")
receiver.receive_muc("chat_room@conference.valouzze.local")

#Réception sur un client non existant

new_receiver = XMPP_MUC("machin", "valouzze.local", "truc")
new_receiver.receive_muc("chat_room@conference.valouzze.local")
