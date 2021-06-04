import sys
sys.path.insert(1, '/home/test/XMPP/')
from XMPP_API import XMPP_MUC

sender = XMPP_MUC("admin", "valou", "test")
sender.send_muc("Hey everyone !", "chat_test@conference.valou")