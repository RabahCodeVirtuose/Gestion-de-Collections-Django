


Noms et Prénoms avec adresses mails des membres du groupe: 

TOUBAL Rabah : rabah.toubal@etu.univ-orleans.fr
GUILLARD Joan: joan.guillard@etu.univ-orleans.fr
HAMZE Muhamad: muhamad.hamze@etu.univ-orleans.fr
RAHMOUN Merouane: merouane.rahmoun@etu.univ-orleans.fr

Commandes question 01:

USERNAME=$(basename $(id -un) @campus.univ-orleans.fr) USERID=$(id -u) docker-compose up -d
docker exec -ti fw1-cc-votre_nom_utilisateur whoami
django-admin startproject cc 
python manage.py startapp collec_management









___________________________________________________________________
Commande question 04: 
from collec_management.models import Collec

# Ajout de collections
Collec.objects.create(title="Collection Art Moderne", description="Une collection dédiée à l'art moderne.")
Collec.objects.create(title="Vinyles Anciens", description="Collection de vinyles rares et anciens.")
Collec.objects.create(title="Photographies de Voyage", description="Photos prises lors de divers voyages.")
Collec.objects.create(title="Objets d'Artisanat", description="Artisanat du monde entier.")
Collec.objects.create(title="Affiches de Films", description="Affiches de films cultes et rares.")
Collec.objects.create(title="Livres de Science", description="Collection de livres scientifiques.")
Collec.objects.create(title="Cartes Postales Vintage", description="Cartes postales des années 50.")
Collec.objects.create(title="Figurines de Super-Héros", description="Figurines de collection de divers super-héros.")
Collec.objects.create(title="Instruments de Musique", description="Instruments de musique classiques.")
Collec.objects.create(title="Peintures Abstraites", description="Peintures abstraites des années 60.")
Collec.objects.create(title="Photographies Noir et Blanc", description="Collection de photos en noir et blanc.")


pour le fichier JSON
python manage.py dumpdata collec_management.Collec --output=collec_management/fixtures/examples.json --indent=4

_______________________________________________________






213338302AG (je vais le supprimer après)