# CREATION D'UNE API XMPP POUR UN PROJET

> L'API Suivante est basé sur la librairie python "xmpppy" et un serveur Ejabberd. Elle est destinée à simplifier l'envoi de messages XMPP en utilisant python étant donnée qu'aucune librairie vraiment bien documentée n'existe à ce jour pour le protocole XMPP hormis en Java

## Fonctionnalités

L'API possède plusieurs fonctionnalités :

- XMPP Offline queue

Permet d'envoyer et recevoir des messages en mode hors ligne

- XMPP MUC (Multi User Channel)

Permets également l'envoi et la réception de message sur un Multi User Channel, lors de la réception, on peut voir tous les anciens messages qui seront séparés d'un message "None" pour voir les messages reçus après démarrage du client de réception.
Libre à vous par la suite d'ajouter un champ avec la date et l'heure dans votre message afin de pouvoir faire un historique plus clair.

- Ejabberd

Quelques fonctionnalités permettant de gérer votre serveur Ejabberd ont également été implémentée, je vous invite à aller lire la documentation pour en savoir plus

- Autres serveurs

Pour ce qui est des autres serveurs XMPP qu'Ejabberd, il faudra par vous-même faire une nouvelle classe directement dans l'API gérant votre serveur favori (Comme Prosody, OpenFire, etc ...) 

## Documentations

Une documentation au sujet de l'API se trouve dans doc/_build/html
Il suffit de télécharger ce qui s'y trouve et soit de le lancer dans un navigateur, soit d'héberger l'ensemble des fichiers sur un serveur apache

## Demo files

Les demo_files sont ici pour montrer de façon très basique comment fonctionne l'API et comment l'utiliser, pour une utilisation plus poussée, je vous invite à voir l'application de cet API à un projet d'IOT dans le dossier IOT

## IOT

Ici nous avons un peu plus poussé l'API pour montrer ce qu'il était possible de faire sur un projet donné, étant un projet d'étude j'ai pris la liberté d'ajouter le sujet mais le but était ici de remplacer le plus de protocole possible par XMPP (C'est-à-dire remplacer au mieux AMQP et MQTT par XMPP)

## Dépendances

Il vous faudra évidemment un serveur XMPP qui fonctionne pour utiliser cette API ainsi que xmpppy qui s'installe simplement via 
`pip install xmpppy`
