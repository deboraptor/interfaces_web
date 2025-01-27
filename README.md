# Projets pour interfaces web 

## Description du dépôt
Vous trouverez tout d'abord le dossier `api_rest` où les fichiers pour le devoir maison sont présents. 

Les trois devoirs sont les suivants :
* cheeseshop
* zenodo
* philosophy

Je détaille en dessous chaque projet individuellement. 

## Cheeseshop
Le but de cet exercice est de scraper l'[API de PyPI](https://docs.pypi.org/api/json/). On entre un paquet python et on récupère le nom et le mail des auteurs, puis la date de release du paquet.

## Zenodo
<!-- LTeX: language=en-GB -->
> Fichier associé : `fichier.txt`
<!-- LTeX: language=en-GB -->


## Wikipedia trivia
Selon un bruit de couloir, il semblerait que si on clique sur le premier lien de n'importe quel article wikipédia à l'infini, on arrive forcément sur la page "philosophie".


<!-- LTeX: language=en-GB -->
> Wikipedia trivia: if you take any article, click on the first link in the article text not in
> parentheses or italics, **and then repeat**, you will eventually end up at "Philosophy". ([xkcd
> #903](https://xkcd.com/903/))
<!-- LTeX: language=en-GB -->

### L'objectif
On va essayer de créer un petit jeu interactif où l'utilisateur entre le nom d'une page et voit défiler les autres pages jusqu'à la fameuse page "philosophy". 
:white_check_mark: Objectif premier : cliquer sur le premier lien :
- [x] en ignorant les parenthèses
- [x] en ignorant les textes en italiques
Et répéter à l'infini jusqu'à "Philosophy" ! :infinity: 

Pour aller plus loin :
- [ ] essayer de gérer les boucles
    - [ ] si boucle -> cliquer sur le lien juste après
    - [ ] proposer à l'utilisateur ?
- [ ] passer en revue une liste qui contient tous les liens pour pas faire de doublons
- [ ] essayer de faire un graph  
    - [ ] avec networkx 
    - [ ] avec pyvis
    - [ ] avec graphviz