import sys
sys.path.insert(1, '/home/test/XMPP/')
from XMPP_API import XMPP_Offline

sender = XMPP_Offline("test", "valou", "test")
sender.send_message("Hello world ! :)", "admin", "valou")