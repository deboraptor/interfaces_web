### Philosophie

<!-- LTeX: language=en-GB -->
> Wikipedia trivia: if you take any article, click on the first link in the article text not in
> parentheses or italics, **and then repeat**, you will eventually end up at "Philosophy". ([xkcd
> #903](https://xkcd.com/903/))
<!-- LTeX: language=fr -->

- Vérifiez sur une page ou deux si c'est vrai
- Écrivez un script qui prend en argument de ligne de commande un nom de page Wikipédia (en anglais,
  sauf si vous aimez l'aventure) et donne le nombre de sauts nécessaire pour arriver à la page
  *Philosophy* ou une erreur si la page en question n'existe pas.
  - Utilisez l'[API](https://www.mediawiki.org/wiki/API:Get_the_contents_of_a_page) de Wikipédia
    pour obtenir le contenu des pages.
  - Vous pouvez parser le wikitexte à la main ou utiliser
    [wikitextparser](https://pypi.org/project/wikitextparser/)
- Si vous êtes très déterminé⋅es, faites un script qui prend en entrée des pages de Wikipédia et
  produit le graphe (orienté) des pages obtenues en suivant à chaque fois le premier lien de chaque
  page, et ce jusqu'à retomber sur une page déjà visitée. On pourra par exemple utiliser
  [NetworkX](https://networkx.org/documentation/latest/reference/drawing.html), un visualiseur
  interactif comme [pyvis](https://pyvis.readthedocs.io/en/latest/tutorial.html), [un *wrapper* de
  graphviz](https://graphviz.readthedocs.io) ou encore générer directement des fichiers dot.

