from XMPP_API import XMPP_Offline

receiver = XMPP_Offline("test", "localhost", "test")
receiver.receive_message()