from XMPP_API import XMPP_Client

receiver = XMPP_Client("test", "localhost", "test")
receiver.receive_message()