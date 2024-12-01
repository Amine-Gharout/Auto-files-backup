import os
import shutil
import hashlib
from datetime import datetime

def calculer_hash(fichier):
    hasher = hashlib.md5()
    with open(fichier, 'rb') as f:
        while chunk := f.read(4096):
            hasher.update(chunk)
    return hasher.hexdigest()

def sauvegarder_fichier(source, destination):
    if not os.path.exists(destination):
        os.makedirs(destination)
    hash_source = calculer_hash(source)
    destination_fichier = os.path.join(destination, os.path.basename(source))

    if os.path.exists(destination_fichier):
        hash_destination = calculer_hash(destination_fichier)
        if hash_source != hash_destination:
            shutil.copy2(source, destination_fichier)
            print(f"Fichier mis à jour: {source}")
    else:
        shutil.copy2(source, destination_fichier)
        print(f"Fichier sauvegardé: {source}")

def sauvegarde_dossier(source_dossier, destination_dossier):
    for root, dirs, files in os.walk(source_dossier):
        for file in files:
            source_fichier = os.path.join(root, file)
            sauvegarder_fichier(source_fichier, destination_dossier)

# Exemple d'utilisation
source = "/path/to/source"
destination = "/path/to/backup"
sauvegarde_dossier(source, destination)