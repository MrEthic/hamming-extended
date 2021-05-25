# Hamming code simulation

Simulation du code de correction Hamming étendu

## Installation

Installer le package :

```bash
pip install --editable .
```

## Utilisation

Appeler le script :
```bash
hamming [OPTIONS]
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
