import sys
sys.path.insert(1, '/home/test/XMPP/')
from XMPP_API import XMPP_Offline

receiver = XMPP_Offline("admin", "valou", "test")
receiver.receive_message()