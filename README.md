# Anàlisi d'Ús d'Armes de Foc als EUA

Aquest projecte analitza les dades de verificacions d'antecedents per obtenir permisos d'armes de foc als EUA.

## Estructura del Projecte

Aquest projecte es troba en aquest ripositori i té l'estructura següent:
```bash

project/
│
├── data/
│ ├── nics-firearm-background-checks.csv
│ └── us-state-populations.csv
│
├── src/
│ ├── init.py
│ ├── data_processing.py
│ ├── main.py
│
├── README.md
└── requirements.txt
```

## Requisits

Per executar aquest projecte, necessiteu instal·lar les següents llibreries de Python:
pandas
argparse

Podeu instal·lar-les amb pip:
pip install pandas argparse


## Execució

Per executar totes les funcions del projecte:

python src/main.py --all

Per executar funcions específiques:

python src/main.py --read_csv data/nics-firearm-background-checks.csv
python src/main.py --clean_csv data/nics-firearm-background-checks.csv
python src/main.py --rename_col data/nics-firearm-background-checks.csv

## Tests

Actualment, no hi ha tests definits. Podeu afegir tests en el directori `tests` i utilitzar `pytest` per executar-los.

pytest tests/



