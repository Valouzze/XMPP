import sys
sys.path.insert(1, '/home/test/XMPP/')
from XMPP_API import Ejabberd_Server
import time

#Test sur un compte déjà existant
Ejabberd_Server.register_user("test", "valouzze.local", "test")

#Test sur un nouveau compte qui devrait donc fonctionner
Ejabberd_Server.register_user("new", "valouzze.local", "test")

#Test de la liste des utilisateurs dans le domaine "valouzze.local" 
#inclu sur mon serveur ejabberd
Ejabberd_Server.list_of_user("valouzze.local")

#Test pour retirer l'utilisateur créé précedemment
Ejabberd_Server.remove_user("new", "valouzze.local")

#Regardons si l'utilisateur a bien été supprimer
print("\n\n")
Ejabberd_Server.list_of_user("valouzze.local")

#Test pour créer un MUC et l'effacer (ici faire les deux permets 
#de nettoyer l'historique de la conversation)
#Le time.sleep permet une capture d'écran pour montrer qu'il est bien créer
#et présent sur l'interface web
Ejabberd_Server.create_muc("random", "conference.valouzze.local", "valouzze.local")
time.sleep(10)
Ejabberd_Server.delete_muc("random","conference.valouzze.local")
