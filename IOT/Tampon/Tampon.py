import time
import sys
sys.path.insert(1, '/home/test/XMPP/')
from XMPP_API import XMPP_Offline
import threading

server = XMPP_Offline("tampon", "valouzze.local", "test")

def gestion_tampon():
    global server
    while True:
        consumme = server.getLastMessage()
        if consumme != None:
            sender = consumme[1]
            msg = consumme[0]
            print("sender : " + str(sender) + " msg: " + str(msg))
            print('\n')
            if sender == "evt@valouzze.local":
                server.send_message(msg, "backup", "valouzze.local")

receive = threading.Thread(target=server.receive_message)
receive.start()

time.sleep(1)
print("ok")

sending = threading.Thread(target=gestion_tampon)
sending.start()