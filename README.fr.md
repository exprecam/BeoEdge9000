# BeoEdge 9000 — widget multimédia inspiré du Beosound 9000 pour le XENEON EDGE

[English](README.md)

Un lecteur multimédia pour le **XENEON EDGE** de Corsair (iCUE), entièrement dessiné en CSS et
inspiré du changeur de six CD Beosound 9000 de Bang & Olufsen : façade de verre en aluminium
brossé, six baies de disques, une tête de lecture coulissante avec son bouton en métal brossé, un
afficheur en verre noir et un panneau strié anthracite.

> Projet de fan indépendant. Aucun lien avec Bang & Olufsen ni avec Corsair, et aucun soutien de
> leur part — voir [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

<!-- À FAIRE : ajouter une capture prise sur votre XENEON EDGE, puis décommenter :
![BeoEdge 9000 sur le XENEON EDGE](docs/screenshots/preview.png)
-->

## Fonctionnalités

- **Six baies de disques.** Chaque nouveau morceau est « chargé » dans la baie suivante (1 → 6,
  puis on recommence). Revenir à un morceau déjà chargé réactive simplement son disque : les baies
  servent d'historique court, avec la pochette sur chaque disque.
- **Tête de lecture coulissante.** Le bouton et la plaque en aluminium glissent jusqu'au disque en
  cours, rétrécissent et se posent sur son moyeu. Le disque joué garde un liseré ambre et sa LED
  s'allume. Tant qu'aucun morceau n'a été joué, la tête attend en grand sur la baie 1.
- **Disque qui tourne avec de l'inertie.** Il prend de la vitesse au démarrage et ralentit
  progressivement en pause. Vitesse réglable (30 à 400 tr/min).
- **Afficheur en verre noir.** Numéro du disque, titre défilant, artiste, PLAY / PAUSE / STANDBY
  et indicateur de niveau.
- **Horloge de veille.** Sans média, l'afficheur montre l'heure et la date en ambre, au format et
  dans la langue de votre système.
- **Commandes.** Le bouton fait lecture/pause ; les touches précédent / suivant sont gravées dans
  l'afficheur.
- **Trois finitions** (Argent, Anthracite, Noir), lueur ambre ou couleur de la pochette, fond
  personnalisable (couleur, image ou vidéo), image sans média, 12 langues.

## Prérequis

- Windows, avec un **XENEON EDGE**
- **iCUE 5.44 ou plus récent** (le minimum indiqué dans le guide des widgets personnalisés de Corsair)
- Le plugin **Media** (`widgetbuilder.mediadataprovider`, v1.1), fourni par iCUE. Lecture, pause,
  suivant et précédent demandent cette version du plugin.

## Installation

1. Téléchargez `BeoEdge9000-vX.Y.Z.icuewidget` sur la page [Releases](../../releases).
2. Double-cliquez le fichier, **ou** ouvrez le panneau Widgets d'iCUE, cliquez sur **+** et
   choisissez-le.
3. Ajoutez le widget à votre tableau de bord XENEON EDGE. Il est conçu pour le grand format
   (environ 2536×696) et s'adapte aux tailles plus petites.

## Réglages

| Groupe | Réglage | Valeurs |
|--------|---------|---------|
| Personnalisation des médias | Couleur du texte | couleur (blanc par défaut) |
| | Arrière-plan | couleur (`#ebeae6` par défaut) |
| | Image | image ou vidéo de fond |
| | Opacité de l'arrière-plan | 0–100 % |
| | Image sans média | image affichée sur le disque 1 tant qu'aucun morceau n'est chargé |
| Apparence | Finition | Argent, Anthracite, Noir |
| | Couleur de la lueur | Ambre, ou couleur tirée de la pochette |
| | Vitesse du disque | 30–400 tr/min (150 par défaut) |
| Spectre | Afficher le spectre | oui / non |
| | Opacité du spectre | 10–100 % |

## Limites connues

- **L'indicateur de niveau n'analyse pas le son.** iCUE ne transmet pas le signal audio aux
  widgets : les barres sont générées (un rythme dérivé du nom du morceau) et suivent seulement
  lecture / pause.
- Le disque tourne par défaut à 150 tr/min, plus lentement qu'un vrai lecteur CD, pour rester
  lisible à l'écran.
- L'historique des disques est en mémoire : il repart de zéro quand le widget se recharge.
- Les pochettes sont rognées en cercle, et la tête de lecture cache le centre de la pochette du
  disque en cours.
- Le plugin Media ne propose que suivant / précédent : impossible de choisir un disque directement.
- Windows uniquement, comme déclaré dans le manifeste.

## Compiler depuis les sources

Python 3 est nécessaire. Node.js est facultatif (vérification de la syntaxe JavaScript).

```bash
python scripts/check.py   # valide le JSON, les traductions et le JavaScript intégré
python scripts/build.py   # produit dist/BeoEdge9000-vX.Y.Z.icuewidget
```

`build.py` attend quatre fichiers d'aide de Corsair dans `src/libs/`. Ils sont protégés par le
droit d'auteur de Corsair : ils ne sont donc **pas dans ce dépôt**. Copiez-les depuis le
WidgetBuilder Kit de Corsair (ou depuis n'importe quel widget fait avec). Détails dans
[THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

Toute la mise en page est dessinée sur une grille de 355 × 100 (`--u` dans le CSS) et garde donc
ses proportions à toutes les tailles.

## Contribuer

Les tickets et les pull requests sont les bienvenus — voir [CONTRIBUTING.md](CONTRIBUTING.md). Un
nouveau réglage doit être traduit dans toutes les langues de `translation.json` ; `scripts/check.py`
le vérifie.

## Licence

MIT pour l'œuvre originale de ce dépôt — voir [LICENSE](LICENSE). Les fichiers d'aide de Corsair et
les marques citées appartiennent à leurs propriétaires.
