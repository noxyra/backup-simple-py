# Importation des libs requises.
from datetime import date
import os

# Attention : Ne pas oublier de generer les cles RSA.

# Attention les dossiers de BKP doivent deje etre cree
# De preference dans un disque dur dedie (externe ou interne)
path_bkp_folder = "/Users/loginUser/Backups/" # Modifier le dossier selon le client

# Creation des variables utiles

    # Liste des serveurs
serveurs = ["exemple1.tld", "exemple2.tld"]

mkdirsite = "mkdir -p " + path_bkp_folder + "site"
mkdirdata = "mkdir -p " + path_bkp_folder + "db"

dirsite = path_bkp_folder + "site/"
dirdata = path_bkp_folder + "db/"

# Creation des dossiers de recuperation (si non existant)
os.system(mkdirsite)
os.system(mkdirdata)

print "Dossier de recuperation ... OK"

# Recuperation des BKP
print "Recuperation des sauvegardes du jour."

for serveur in serveurs:
    print "Serveur : " + serveur

    cmd = "scp loginUser@" + serveur + ":/home/loginUser/backup/site/*.zip " + dirsite

    os.system(cmd)

    print "Sites ... OK"

    cmd = "scp loginUser@" + serveur + ":/home/loginUser/backup/db/*.sql " + dirdata

    os.system(cmd)

    print "Bases de donnees ... OK"

print "Recuperation des sauvegardes terminee"
