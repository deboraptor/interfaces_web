## 1
# voir si la page existe sur wikipédia
# y'a une API ! et gratuite
# -> wikitextparser
## 2
# il faut prendre un autre lien, mais faut qu'il soit valide ! 
# donc test http code = 200
## 3
# compter combien de liens on a pour philosophy
## 4
# afficher le nombre de liens qu'on a parcouru !

"""
- Écrivez un script qui prend en argument de ligne de commande un nom de page Wikipédia et donne 
  le nombre de sauts nécessaire pour arriver à la page
  Philosophy ou une erreur si la page en question n'existe pas.
  - Utilisez l'API de Wikipédia pour obtenir le contenu des pages.
  - Vous pouvez parser le wikitexte à la main ou utiliser wikitextparser.
- Si vous êtes très déterminé⋅es, faites un script qui prend en entrée des pages de Wikipédia et
  produit le graphe (orienté) des pages obtenues en suivant à chaque fois le premier lien de chaque
  page, et ce jusqu'à retomber sur une page déjà visitée. On pourra par exemple utiliser
  NetworkX, un visualiseur interactif comme pyvis, un wrapper de graphviz ou encore générer directement 
  des fichiers dot.
"""

import requests
import wikitextparser as wtp
import time

WIKI_API_URL = "https://en.wikipedia.org/w/api.php"
PHILOSOPHY = "Philosophy"

def get_pages_revisions(title):
    """ Vérifie si la page existe et récupère son le titre et le contenu """

    params = {
        "action": "query",
        "format": "json",
        "prop": "revisions",
        "titles": title,
        "rvprop": "content",
        "rvslots": "main"
    }
    requests_session = requests.Session()
    response = requests_session.get(WIKI_API_URL, params=params)
    data = response.json()
    
    page = next(iter(data["query"]["pages"].values()))
    if "missing" in page:
        print(f"❌ La page '{title}' n'existe pas.")
        return None
    
    return page["revisions"][0]["slots"]["main"]["*"]

def nettoyage_scraping(wikitext):
    """ Nettoie le wikitext pour retirer les footnotes et images """

    parsed = wtp.parse(wikitext)

    # on enlève les gros paragraphes (footnotes) avant le vrai corps de la page
    text_blocks = [section.string for section in parsed.sections if section.string.strip()]

    if not text_blocks:
        return None 

    return text_blocks[0] 

def extraction_premier_lien(wikitext):
    """ Extrait le premier lien valide, en évitant les fichiers et liens spéciaux """
    
    parsed = wtp.parse(wikitext)
    for link in parsed.wikilinks:
        title = link.title

        # on skip les fichiers et le reste sinon ça bug
        if title.startswith(("File:", "Image:", "Media:", "Special:", "Help:", "Wikipedia:")):
            continue

        return title  

    return None

def check_lien_correct(title):
    """ Vérifie si un lien mène à une page valide (HTTP code = 200) """

    response = requests.get(f"https://en.wikipedia.org/wiki/{title}")
    return response.status_code == 200

def compte_liens_philosophy(start_page):
    """ Compte les liens jusqu'à Philosophy """

    visited = set()
    page_actuelle = start_page
    nombre_page = 0

    while page_actuelle.lower() != PHILOSOPHY.lower():
        if page_actuelle in visited:
            print("🔁 On tourne en rond !! On arrête")
            return
        
        print(f"🔗 {nombre_page} : {page_actuelle}")
        visited.add(page_actuelle)

        wikitext = get_pages_revisions(page_actuelle)
        if not wikitext:
            print("❌ Impossible de récupérer la page...")
            return

        prochain_lien = extraction_premier_lien(wikitext)
        if not prochain_lien:
            print("🚫 Aucun lien valide trouvé...")
            return
        
        page_actuelle = prochain_lien.replace("_", " ")
        nombre_page += 1
        time.sleep(0.5)  

    print(f"🎉 Arrivé à 'Philosophy' en {nombre_page} étapes !")

if __name__ == "__main__":
    # rendre le jeu un peu plus simple
    start_page = input("🔎 Entrez le nom de la page Wikipédia : ").replace(" ", "_")
    compte_liens_philosophy(start_page)
