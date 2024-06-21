# src/main.py

import argparse
from data_processing import read_csv, clean_csv, rename_col, breakdown_date, erase_month

def main():
    parser = argparse.ArgumentParser(description="Anàlisi de dades d'ús d'armes de foc als EUA")
    parser.add_argument('--all', action='store_true', help='Executa totes les funcions')
    parser.add_argument('--read_csv', type=str, help='Llegeix un fitxer CSV des d\'una ruta de fitxer')
    parser.add_argument('--clean_csv', type=str, help='Neteja el dataset eliminant columnes innecessàries')
    parser.add_argument('--rename_col', type=str, help='Canvia el nom de la columna longgun per long_gun')
    parser.add_argument('--breakdown_date', type=str, help='Divideix la columna month en year i month')
    parser.add_argument('--erase_month', type=str, help='Elimina la columna month')

    args = parser.parse_args()

    if args.all or args.read_csv:
        # Llegir el fitxer CSV
        if args.read_csv:
            filepath = args.read_csv
        else:
            filepath = '../data/nics-firearm-background-checks.csv'  # Substituir per la ruta correcta
        df = read_csv(filepath)

    if args.all or args.clean_csv:
        # Netejar el dataset
        if not args.all:
            df = read_csv(args.clean_csv)  # Llegir el fitxer si només s'executa clean_csv
        df_cleaned = clean_csv(df)

    if args.all or args.rename_col:
        # Canviar el nom de la columna
        if not args.all:
            df = read_csv(args.rename_col)  # Llegir el fitxer si només s'executa rename_col
        df_cleaned = rename_col(df)

    if args.all or args.breakdown_date:
        # Dividir la columna month en year i month
        if not args.all:
            df = read_csv(args.breakdown_date)  # Llegir el fitxer si només s'executa breakdown_date
        df_cleaned = breakdown_date(df)

    if args.all or args.erase_month:
        # Eliminar la columna month
        if not args.all:
            df = read_csv(args.erase_month)  # Llegir el fitxer si només s'executa erase_month
        df_cleaned = erase_month(df)

if __name__ == '__main__':
    main()
