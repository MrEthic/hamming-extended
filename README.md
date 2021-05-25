# Hamming code simulation

Simulation du code de correction Hamming étendu :
https://github.com/MrEthic/hamming-extended

## Version
Simulation dévelppé en Python 3.7

## Installation

Installer le package :

```bash
pip install --editable .
```

## Utilisation

Appeler le script installé :
```bash
hamming [OPTIONS]
```
Appeler le script sans installation :
```bash
pip install Click, numpy
python3 hamming.py [OPTIONS]
```
Options :
```python
Usage: hamming [OPTIONS]

Options:
  -L, --size TEXT    Taille du message  [default: 26]
  -e, --error FLOAT  Taux d'erreur voulu  [default: 0.05]
  -D, --demo TEXT    Forcer une erreur par bloc  [default: 0]
  --help             Show this message and exit.
```

## Auteur
Jérémie Basso (60123) pour G5E
