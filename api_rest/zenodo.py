import os
import requests
from config import Config

ACCESS_TOKEN = Config.ACCESS_TOKEN
ZENODO_API = Config.ZENODO_API

def create_deposit(title, author):
    headers = {"Content-Type": "application/json"}
    params = {"access_token": ACCESS_TOKEN}

    data = {
        "metadata": {
            "title": title,
            "upload_type": "dataset",
            "description": "Dépôt automatique via API Zenodo",
            "creators": [{"name": author}]
        }
    }

    response = requests.post(ZENODO_API, json=data, params=params, headers=headers)

    if response.status_code == 201:
        deposit_id = response.json()["id"]
        return deposit_id
    else:
        print("❌ Erreur lors de la création du dépôt :", response.json())
        return None

def upload_file(deposit_id, file_path):
    params = {"access_token": ACCESS_TOKEN}
    files_url = f"{ZENODO_API}/{deposit_id}/files"

    if not os.path.isfile(file_path):
        print(f"❌ Erreur : le fichier '{file_path}' n'existe pas. Vérifie le chemin !")
        return

    with open(file_path, "rb") as file:
        files = {"file": (file_path, file)}
        response = requests.post(files_url, params=params, files=files)

    if response.status_code == 201:
        print("✅ Fichier uploadé avec succès !")
    else:
        print("❌ Erreur lors de l'upload du fichier :", response.json())

def publish_deposit(deposit_id):
    params = {"access_token": ACCESS_TOKEN}
    publish_url = f"{ZENODO_API}/{deposit_id}/actions/publish"

    response = requests.post(publish_url, params=params)

    if response.status_code == 202:
        deposit_url = response.json()["links"]["html"]
        print(f"✅ Dépôt publié avec succès ! Lien : {deposit_url}")
    else:
        print("❌ Erreur lors de la publication du dépôt :", response.json())

file_path = input("Nom du fichier à déposer : ")
title = input("Titre du dépôt : ")
author = input("Nom de l'auteurice : ")

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, file_path)

print("\n📌 Création du dépôt...")
deposit_id = create_deposit(title, author)

if deposit_id:
    print("\n📤 Upload du fichier...")
    upload_file(deposit_id, file_path)

    print("\n🚀 Publication du dépôt...")
    publish_deposit(deposit_id)