import httpx

def get_package():
    package_name = input("🔍️ Choisissez un paquet à observer : ")
    try:
        response = httpx.get(f"https://pypi.org/pypi/{package_name}/json", follow_redirects=True)

        if response.status_code == 404:
            print("❌️ Ce package n'existe pas.")
            return

        link = response.json()

        #print("Le dictionnaire a cette forme :")
        #for cle, valeur in link.items():
        #    print(cle, valeur)

        print("\n📄 On veut récupérer le nom des auteurices du package :")
        print(link["info"].get("author", "Auteur inconnu"))

        print("\n📩 Maintenant leur mail :")
        print(link["info"].get("author_email", "Email inconnu"))

        print("\n🛠️  Et la dernière release :")
        if link["releases"]:
            derniere_release = list(link["releases"])[-1]
            print(derniere_release)

            print("\n📅 Avec la date de celle-ci :")
            upload_time = link["releases"][derniere_release][-1]
            print(upload_time.get("upload_time", "Date inconnue"))
        else:
            print("❌️ Aucune release disponible.")

    except httpx.RequestError as e:
        print(f"🚫 Erreur lors de la requête : {e}")

    except Exception as e:
        print(f"🚫 Une erreur inattendue s'est produite : {e}")

get_package()