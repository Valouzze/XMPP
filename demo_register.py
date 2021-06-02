from XMPP_API import *

#Test sur un compte déjà existant
#register_user("test", "valou", "test")

#Test sur un nouveau compte qui devrait donc fonctionner
#register_user("new", "valou", "test")

#Test pour retirer l'utilisateur créé précedemment
#remove_user("new", "valou")

#Test de la liste des utilisateurs dans le domaine "valou" inclu sur mon serveur ejabberd
#list_of_user("valou")

#Test pour créer un MUC et l'effacer (ici faire les deux permets de nettoyer l'historique de la conversation)
delete_muc("chat_test","conference.valou")
create_muc("chat_test", "conference.valou", "valou")