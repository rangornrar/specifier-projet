# Contribuer

Les corrections de consignes, exemples réalistes et améliorations de documentation sont bienvenues. Pour un changement de comportement, décrivez d'abord le cas concret et son effet attendu dans une issue.

## Préparer une modification

1. Créer une branche dédiée, par exemple `docs/clarifier-installation`.
2. Limiter la modification au problème décrit.
3. Mettre à jour les guides ou exemples concernés et l'entrée « Non publié » du [changelog](CHANGELOG.md).
4. Exécuter les contrôles ci-dessous.
5. Ouvrir une pull request avec le problème, le comportement obtenu et les vérifications effectuées.

## Conventions

- Rédiger les consignes et guides en français, en UTF-8 avec des fins de ligne LF.
- Garder `SKILL.md` comme référence du comportement et placer les détails conditionnels dans les ressources adaptées.
- Préserver les distinctions entre fait, hypothèse, proposition et décision explicitement acceptée.
- Ne pas inventer de réponses utilisateur, de validation, de coût ou de délai.
- Conserver une profondeur proportionnée à un petit projet.
- Ne pas introduire de dépendance à un outil qui ne sert pas réellement le workflow.
- Utiliser des projets fictifs ou des éléments anonymisés dans les exemples et signalements.

## Vérifier

Depuis la racine du dépôt, avec Python 3.10 ou plus récent :

```sh
python -m pip install -r requirements-dev.txt
python scripts/validate_repository.py
```

Le contrôle vérifie les fichiers YAML, les métadonnées essentielles, les ressources locales et les liens Markdown vers des fichiers. Il ne vérifie pas la disponibilité des sites externes ni la qualité d'une réponse produite par un modèle.

Si les instructions changent, exécuter les scénarios pertinents de [recette manuelle](docs/VALIDATION.md). Indiquer dans la PR ceux réalisés, l'environnement utilisé et les limites. Si un PDF est produit, inspecter son rendu avant de le joindre.

## Revue

Une PR doit expliquer le problème observable, la solution et les éventuels compromis. Préserver les décisions existantes sauf justification explicite. Une proposition de licence ou de changement de distribution doit faire l'objet d'un choix de l'auteur.
