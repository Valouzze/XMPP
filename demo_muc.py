from XMPP_API import XMPP_MUC

receiver = XMPP_MUC("admin", "valou", "test")
receiver.receive_muc("chat_test@conference.valou")
