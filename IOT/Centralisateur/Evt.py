import sys
sys.path.insert(1, '/home/test/XMPP/')
from XMPP_API import XMPP_Offline
import threading
import time

client = XMPP_Offline("evt", "valouzze.local", "test")

def sending():
    global client
    while True:
        consumme = client.getLastMessage()
        if consumme != None :
            sender = consumme[1]
            msg = consumme[0]
            if sender == "passerelle@valouzze.local":
                print("sender : " + str(sender) + " msg: " + str(msg))
                client.send_message(msg, "web", "valouzze.local")
                client.send_message(msg, "tampon", "valouzze.local")

receive = threading.Thread(target=client.receive_message)
receive.start()

sending_message = threading.Thread(target=sending())
sending.start()