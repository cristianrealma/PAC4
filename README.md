## Context

Els elements d'aquest repositori constitueixen la resposta a la PAC 4 de l'assignatura *Programació per a la ciència de dades* del *Màster en Ciència de Dades* de la [Universitat Oberta de Catalunya](https://www.uoc.edu/portal/ca/index.html) (UOC), corresponent al curs 2023-2024.

# Anàlisi d'Ús d'Armes de Foc als EUA

Aquest projecte analitza les dades de verificacions d'antecedents per obtenir permisos d'armes de foc als EUA.

## Estructura del Projecte

Aquest projecte es troba en aquest ripositori i té l'estructura següent:
```bash

pac/
│
├── data/
│ ├── nics-firearm-background-checks.csv
│ ├── us-state-populations.csv
│ └── us-state.json
│
├── src/
│ ├── __init__.py
│ ├── data_processing.py
│ ├── main.py
│ └── visualization.py
│
├── LICENSE.txt
├── README.md
├── requirements.txt
```

### Instruccions per executar *main.py*

1. `Cal obrir un terminal i situar-se al directori destinat al projecte`
2. `git clone https://github.com/cristianrealma/PAC4.git`
3. `cd ./aprenent-python/pac`
4. `Crear un entorn virtual i activar-lo`
5. `pip install -r requirements.txt`
6. `python3 ./main.py`&emsp;&emsp;&emsp;

   
## Requisits

Per executar aquest projecte, necessiteu instal·lar les següents llibreries de Python:
pandas
argparse
matplotlib

Podeu instal·lar-les amb pip:
pip install pandas argparse matplotlib

### Requeriments
- Python 3.x
- Pandas
- Folium
- Selenium
- Pillow
- Chrome WebDriver

## Instal·lació de dependències


pip install pandas folium selenium pillow

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
python src/main.py --time_evolution data/nics-firearm-background-checks.csv
python src/main.py --groupby_state data/nics-firearm-background-checks.csv
python src/main.py --clean_states data/nics-firearm-background-checks.csv
python src/main.py --merge_datasets data/nics-firearm-background-checks.csv data/us-state-populations.csv
python src/main.py --calculate_relative_values data/nics-firearm-background-checks.csv
python src/main.py --analyze_data data/nics-firearm-background-checks.csv

## Tests

pytest tests/

## Comentaris

Comentari del l'exercici 4.2: el gràfic generat mostrarà l'evolució temporal del nombre de permisos, pistoles i rifles d'assalt registrats als EUA des del 1998 fins al 2020. Podreu observar tendències ascendent o descendent en les dades, així com canvis durant períodes específics com la pandèmia del 2020.

## Llicència
The MIT License (MIT)

Copyright (c) 2024 UOC

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

