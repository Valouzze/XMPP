from XMPP_API import XMPP_Client

sender = XMPP_Client("admin", "localhost", "test")
sender.send_message("Hello world ! :)", "test", "localhost")