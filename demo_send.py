from XMPP_API import XMPP_Offline

sender = XMPP_Offline("test", "valou", "test")
sender.send_message("Hello world ! :)", "admin", "valou")