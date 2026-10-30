# Utiliser Spécifier un projet

## Préparer le contexte

Décrivez le problème rencontré, les personnes concernées et un exemple d'utilisation de bout en bout. Joignez les documents existants et indiquez leur version. Partagez les contraintes connues : plateforme, fonctionnement hors connexion, données, intégrations, budget ou délai réellement imposé.

Si une information manque, dites-le. Le skill peut proposer des options techniques, mais doit conserver la différence entre une recommandation et une décision acceptée.

## Avancer par étapes

1. **Cadrage** : préciser le problème, la cible, les objectifs et les usages prioritaires.
2. **Entretien** : répondre à une à trois questions par échange. Signaler ce qui est décidé, incertain ou hors périmètre.
3. **Premier audit** : examiner les lacunes et risques d'un ensemble cohérent de spécifications.
4. **Arbitrages** : répondre aux questions issues de l'audit ; accepter, refuser ou modifier les propositions.
5. **Consolidation** : stabiliser la V1 et ses critères d'acceptation. Les inconnues restantes sont consignées dans une version provisoire.
6. **Livraison** : obtenir un PDF vérifié, sa source éditable et l'état nécessaire à la reprise.

Il est possible de demander un PDF de travail avant stabilisation. Le document doit alors annoncer son statut et ses points ouverts.

## Comprendre les identifiants

| Préfixe | Élément suivi |
| --- | --- |
| OBJ | Objectif |
| F | Fonction |
| RG | Règle métier |
| NF | Exigence non fonctionnelle |
| TECH | Contrainte technique |
| DEC | Décision |
| AUD | Constat d'audit |
| Q | Question ouverte |
| REC | Critère ou scénario de recette |

Les identifiants restent stables entre deux versions. Une suppression ou un remplacement est signalé plutôt que de renuméroter le dossier.

## Exemple de traçabilité

Exemple fictif pour un outil de prêt de matériel :

- **OBJ-001** : savoir quel matériel est actuellement prêté.
- **F-001** : enregistrer un prêt avec le matériel, l'emprunteur et la date.
- **Q-001** : un même matériel peut-il avoir plusieurs prêts ouverts ?
- **RG-001**, après réponse explicite : un seul prêt ouvert par matériel.
- **REC-001** : étant donné un matériel déjà prêté, quand un utilisateur tente d'ouvrir un second prêt, alors l'enregistrement est refusé avec un message compréhensible.

Cette règle illustre une décision possible. Elle doit être confirmée pour le projet réel.

## Demander une revue utile

Fournissez une version précise du dossier et indiquez ce qui a changé depuis la dernière revue. Demandez des constats fondés sur des exigences identifiables, leur conséquence et les questions permettant de les résoudre.

Les huit regards sont des grilles d'analyse d'une IA. Un audit complet peut indiquer qu'un regard n'a pas de constat matériel. La synthèse conserve les désaccords utiles et ordonne les questions ; elle ne valide pas le dossier à votre place.

## Produire le dossier

Le [plan de référence](../references/plan-dossier.md) couvre le besoin, la cible, les spécifications générales et détaillées, les données, les exigences non fonctionnelles, les choix techniques, la méthode, l'audit et la recette.

La livraison attendue comprend :

- Le PDF avec version, date, statut, sommaire paginé et conclusion.
- Une source éditable du dossier.
- L'état de reprise : décisions, hypothèses, risques, exigences et questions ouvertes.
- Les réserves et prochaines questions lorsque le travail continue.

Le format éditable dépend de l'environnement ; si vous souhaitez un DOCX, précisez-le. Les tableaux, caractères et sauts de page doivent être inspectés sur le rendu PDF. Si la génération est indisponible, l'assistant doit expliquer la limite et conserver les éléments de travail accessibles.

## Reprendre une autre fois

Conservez le PDF, sa source et l'état de reprise dans votre espace de travail. Lors de la reprise, indiquez le dernier dossier de référence et demandez de lire ces fichiers avant de poser de nouvelles questions. Une conversation seule ne remplace pas cette sauvegarde.

## Dépannage

| Situation | Action |
| --- | --- |
| Skill absent du sélecteur | Vérifier le dossier d'installation et la présence de `SKILL.md`, puis redémarrer le client si nécessaire. |
| Deux skills portant le même nom | Vérifier les installations personnelles et celles du projet pour identifier les doublons. |
| Questions déjà traitées | Fournir le dernier état de reprise et les décisions correspondantes. |
| Audit répétitif | Demander de dédupliquer les constats et de réexaminer uniquement les changements et leurs impacts. |
| PDF indisponible | Vérifier la présence des capacités PDF et de sauvegarde ; demander la source et le registre des points ouverts. |

Pour contribuer à une correction, suivre le [guide de contribution](../CONTRIBUTING.md).
