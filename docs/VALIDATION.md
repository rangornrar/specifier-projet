# Validation et recette

## Contrôles automatiques

```sh
python -m pip install -r requirements-dev.txt
python scripts/validate_repository.py
```

Le même script est lancé par [GitHub Actions](../.github/workflows/validate.yml) sur les pushes et pull requests. Il contrôle :

- Le frontmatter YAML et le nom du skill.
- Les métadonnées d'interface et les chemins d'icônes.
- La syntaxe des fichiers YAML du dépôt.
- La présence des ressources de base et de la documentation principale.
- Les cibles locales des liens Markdown, hors blocs de code.
- La bonne formation XML de l'icône SVG.

Les liens Web et les ancres internes ne sont pas validés. Ces contrôles statiques ne prouvent pas la qualité des spécifications ni du rendu PDF.

## Recette du comportement

Utiliser des données fictives et une conversation distincte par scénario. Noter la révision du skill, le client, le modèle, les capacités disponibles, le résultat et les écarts. Ne pas déduire une réussite d'un simple mot-clé dans une réponse.

| Scénario | Mise en situation | Résultat observable attendu |
| --- | --- | --- |
| Idée peu définie | Demander de cadrer « un outil simple pour une association ». | L'assistant demande le problème, la cible et un cas concret, sans rédiger de faux dossier complet. |
| Réponse imprécise | Répondre « rapide et sécurisé », sans seuil ni contexte. | L'assistant demande des comportements ou critères observables ; les seuils inconnus restent ouverts. |
| Cahier des charges existant | Fournir une fonction sans règle de droit ni cas d'erreur. | L'audit identifie les lacunes précises, leurs conséquences et les questions utiles, sous les regards pertinents. |
| Choix technique inconnu | Donner une contrainte hors connexion sans technologie imposée. | Les options sont liées au besoin, leurs compromis sont expliqués et le choix reste proposé. |
| Décision différée | Ne pas répondre à une recommandation d'architecture. | Le dossier conserve le statut proposé ou à déterminer ; l'absence de réponse ne vaut pas validation. |
| Périmètre modifié | Reporter une fonction V1 après un premier audit. | Les exigences, dépendances, critères de recette et constats touchés sont actualisés en conservant les identifiants. |
| PDF demandé tôt | Demander un PDF alors que des questions restent ouvertes. | Un dossier de travail est livré si les outils le permettent, avec statut et réserves visibles. |
| Outils PDF absents | Exécuter dans un environnement sans capacité de génération/rendu. | La limite est annoncée ; aucun faux lien de PDF n'est présenté. |
| Reprise | Fournir un dossier et son état de reprise dans une nouvelle conversation. | Les sources sont lues et les décisions closes ne sont pas redemandées sans fait nouveau. |
| Hors périmètre | Demander uniquement une correction ponctuelle de code sans cadrage. | Le skill n'est pas choisi implicitement pour imposer un entretien de spécification. |

## Contrôle du livrable PDF

Vérifier le contenu convenu et le statut réel, les identifiants, les critères d'acceptation et les points ouverts. Contrôler la couverture, le sommaire après mise en page, la pagination et les liens utiles. Inspecter les pages rendues pour repérer les coupures, tableaux illisibles, pages vides involontaires et caractères manquants.

Conserver le PDF, la source éditable et l'état de reprise. Consigner toute capacité absente. Une réussite des contrôles statiques ne permet pas de déclarer cette recette PDF réalisée.
