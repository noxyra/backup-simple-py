# Importation des libs requises.
from datetime import date
import os

# Creation des dossiers (si non existant)
os.system("mkdir -p /root/backup/site")
os.system("mkdir -p /root/backup/db")

os.system("mkdir -p /home/loginUser/backup/site")
os.system("mkdir -p /home/loginUser/backup/db")

print "Dossiers de backup ... OK"

# On clean le dossier de bkp.
os.system("rm -rf /root/backup/site/*.zip")
os.system("rm -rf /root/backup/db/*.sql")

print "Purge des backup ... OK"

# Definition des variables utiles.

    #date.
datetime = date.today()

year = str(datetime.year)
month = str(datetime.month)
day = str(datetime.day)

today = year + "-" + month + "-" + day

    #chemin d'acces.
roo_path_site = "/root/backup/site/"
roo_path_data = "/root/backup/db/"

pre_path_site = "/var/www/"
pst_path_site = "/web/"

dst_path_site = "/home/loginUser/backup/site/"
dst_path_data = "/home/loginUser/backup/db/"

    #infos sauvegarde.
sites = ["exemple1.tld", "exemple2.tld"]
databases = ["piwik", "roundcube", "sonity", "sonitydev", "sonityv3"]

    #infos mysql (root acces)
db_user = "root"
db_pass = "Pn2snkillerjr83"

print "Programme initialise."
print "Debut sauvegarde sites internet"

# Debut programme.

    # Pour chaque sites on cree une archive .zip dans /root/backup/site/.
for site in sites:

    print "Sauvegarde du site : " + site

    # Creation des chemins d'acces
    origin_path = pre_path_site + site + pst_path_site
    destin_path = roo_path_site + site + '-' + today + ".zip"

    # Creation de la commande
    cmd = "zip -rq " + destin_path + " " + origin_path

    # Execution !
    os.system(cmd)


print "Sauvegarde sites internet ... OK"
print "Debut sauvegarde bases de donnees."

for db in databases:

    print "Sauvegarde de la bdd de : " + db

    # Creation des chemins d'acces
    destin_path = roo_path_data + db + "-" + today + ".sql"

    # Creation de la commance
    cmd = "mysqldump -u root -h localhost " + db + " > " + destin_path

    # Execution !
    os.system(cmd)


print "Sauvegarde bases de donnees ... OK"

# Deplacement des sauvegardes vers repertoire de recuperation.
print "Deplacement des sauvegardes vers leurs repertoire de recuperation"

site_cmd = "mv " + roo_path_site + "*.zip " + dst_path_site
data_cmd = "mv " + roo_path_data + "*.sql " + dst_path_data

os.system(site_cmd)
os.system(data_cmd)

# Application des bons droit sur les dossiers de recuperations
print "Application des droits sur les dossiers de recuperation"
os.system("chown -R loginUser /home/loginUser/")


print "Sauvegarde terminee !! :)"
