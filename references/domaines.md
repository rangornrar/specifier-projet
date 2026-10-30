# Domaines de questions

Utiliser comme aide de couverture, pas comme questionnaire à envoyer en bloc. Choisir une à trois questions selon leur effet sur la décision. Ne pas reposer ce qui est connu ; consigner les inconnues.

## Besoin et cible

- Quel problème est rencontré aujourd'hui, comment est-il traité et pourquoi changer ?
- Quel résultat concret indiquera que l'outil est utile ?
- Qui utilise, administre, finance, maintient ou subit les effets de l'outil ?
- Quels usages sont prioritaires, exclus ou reportés ? Quelles contraintes de temps et de budget sont réelles ?
- Peut-on décrire un exemple représentatif de bout en bout, puis une exception ?

## Fonctionnement général et détaillé

- Quels rôles, droits, parcours et états existent ? Qui déclenche chaque action ?
- Quelles entrées, validations, règles métier, sorties et formats d'export sont attendus ?
- Que se passe-t-il en cas d'annulation, erreur, doublon, accès refusé ou donnée absente ?
- Faut-il gérer historique, concurrence, synchronisation, reprise ou suppression ?
- Qu'est-ce qui est indispensable en V1 ? Comment vérifier objectivement chaque fonction ?

## Plateforme et OS de destination

- Application web, bureau, mobile, extension, ligne de commande ou service ? Pourquoi ?
- Windows, macOS, Linux, Android, iOS : quels systèmes, versions, navigateurs et appareils doivent être supportés ?
- Usage local, réseau interne ou Internet ; fonctionnement hors connexion ; mono/multi-utilisateur ?
- Matériel, ressources, droits d'installation, distribution et mises à jour disponibles ?
- Contraintes d'hébergement, localisation des données, identité et réseau de l'organisation ?

## Architecture envisagée

- Architecture logique minimale : composants, responsabilités, flux et frontières de confiance.
- Interface, métier et persistance : séparation utile au projet, sans couches gratuites.
- Application locale, monolithe web, client/serveur ou services : quels besoins justifient le choix ?
- Interfaces externes, contrats API, formats, authentification, quotas, erreurs et indisponibilité.
- Dépendances imposées, contraintes d'intégration, réversibilité et migration.
- Décrire les principaux compromis ; représenter les composants seulement si cela clarifie la solution.

## Langages, frameworks et outils

- Technologies imposées, compétences de l'équipe, environnement existant et contraintes de maintenance ?
- Langages côté interface et métier, stockage, bibliothèques et outils de construction nécessaires ?
- Justifier les choix par l'usage, la durée de support, la simplicité, les licences et l'écosystème.
- Vérifier versions, compatibilités, support et limites auprès des sources officielles au moment du choix.
- Laisser les versions non vérifiées « à confirmer » ; ne pas confondre préférence et exigence.

## Données et sécurité

- Entités, relations, sources, volumes, qualité, import/export, conservation et suppression ?
- Données personnelles ou sensibles, utilisateurs autorisés, droits et journalisation ?
- Authentification, gestion des secrets, chiffrement et dépendances selon le contexte réel.
- Sauvegarde, restauration, réversibilité et propriété des données.
- Obligations applicables seulement si établies ; distinguer recommandations de sécurité et obligations.

## Qualités attendues et exploitation

- Quels volumes, temps de réponse, accessibilité, disponibilité et compatibilité sont nécessaires ?
- Qui installe, met à jour, surveille, dépanne et répond aux utilisateurs ?
- Environnements, configuration, logs, supervision, sauvegarde et retour arrière ?
- Coûts récurrents, licences, hébergement, maintenance, dépendance fournisseur ?
- Quelle recette rendra la première version acceptable ? Qui statue sur cette recette ?

## Méthode de réalisation

- Réalisation seul, en équipe ou avec prestataire ; niveau d'expérience et disponibilité ?
- Découpage V1/incréments, démonstrations et validation des scénarios prioritaires.
- Gestion du code et des versions, revue, documentation et suivi des décisions.
- Tests unitaires, intégration, bout en bout et recette selon les risques ; automatisation proportionnée.
- Prototypes ou essais ciblés pour lever une incertitude avant engagement architectural.
- Livraison, retour arrière, support et gestion des demandes d'évolution.
- Si l'IA est utilisée pour coder, préciser ce qui sera relu et vérifié par des tests et une recette.
