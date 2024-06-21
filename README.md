## Context

Els elements d'aquest repositori constitueixen la resposta a la PAC 4 de l'assignatura *Programació per a la ciència de dades* del *Màster en Ciència de Dades* de la [Universitat Oberta de Catalunya](https://www.uoc.edu/portal/ca/index.html) (UOC), corresponent al segon semestre del curs 2023-2024.

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
python src/main.py --breakdown_date data/nics-firearm-background-checks.csv
python src/main.py --erase_month data/nics-firearm-background-checks.csv
python src/main.py --groupby_state_and_year data/nics-firearm-background-checks.csv
python src/main.py --print_biggest_handguns data/nics-firearm-background-checks.csv
python src/main.py --print_biggest_longguns data/nics-firearm-background-checks.csv

## Tests

Actualment, no hi ha tests definits. Podeu afegir tests en el directori `tests` i utilitzar `pytest` per executar-los.

pytest tests/



