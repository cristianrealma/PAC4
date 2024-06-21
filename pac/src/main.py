# src/main.py

import argparse
from data_processing import (
    read_csv,
    clean_csv,
    rename_col,
    breakdown_date,
    erase_month,
    groupby_state_and_year,
    print_biggest_handguns,
    print_biggest_longguns,
    time_evolution
)

def main():
    parser = argparse.ArgumentParser(description="Anàlisi de dades d'ús d'armes de foc als EUA")
    parser.add_argument('--all', action='store_true', help='Executa totes les funcions')
    parser.add_argument('--read_csv', type=str, help='Llegeix un fitxer CSV des d\'una ruta de fitxer')
    parser.add_argument('--clean_csv', type=str, help='Neteja el dataset eliminant columnes innecessàries')
    parser.add_argument('--rename_col', type=str, help='Canvia el nom de la columna longgun per long_gun')
    parser.add_argument('--breakdown_date', type=str, help='Divideix la columna month en year i month')
    parser.add_argument('--erase_month', type=str, help='Elimina la columna month')
    parser.add_argument('--groupby_state_and_year', type=str, help='Agrupa el dataframe per estat i any')
    parser.add_argument('--print_biggest_handguns', type=str, help='Imprimeix l\'estat i l\'any amb el nombre més gran de hand_guns')
    parser.add_argument('--print_biggest_longguns', type=str, help='Imprimeix l\'estat i l\'any amb el nombre més gran de long_guns')
    parser.add_argument('--time_evolution', type=str, help='Crea un gràfic amb l\'evolució temporal de permit, handgun i long_gun')

    args = parser.parse_args()

    if args.all or args.read_csv:
        if args.read_csv:
            filepath = args.read_csv
        else:
            filepath = '../data/nics-firearm-background-checks.csv'
        df = read_csv(filepath)

    if args.all or args.clean_csv:
        if not args.all:
            df = read_csv(args.clean_csv)
        df_cleaned = clean_csv(df)

    if args.all or args.rename_col:
        if not args.all:
            df = read_csv(args.rename_col)
        df_cleaned = rename_col(df)

    if args.all or args.breakdown_date:
        if not args.all:
            df = read_csv(args.breakdown_date)
        df_cleaned = breakdown_date(df)

    if args.all or args.erase_month:
        if not args.all:
            df = read_csv(args.erase_month)
        df_cleaned = erase_month(df)

    if args.all or args.groupby_state_and_year:
        if not args.all:
            df = read_csv(args.groupby_state_and_year)
        df_grouped = groupby_state_and_year(df_cleaned)

    if args.all or args.print_biggest_handguns:
        if not args.all:
            df_grouped = groupby_state_and_year(read_csv(args.print_biggest_handguns))
        print_biggest_handguns(df_grouped)

    if args.all or args.print_biggest_longguns:
        if not args.all:
            df_grouped = groupby_state_and_year(read_csv(args.print_biggest_longguns))
        print_biggest_longguns(df_grouped)

    if args.all or args.time_evolution:
        if not args.all:
            df = read_csv(args.time_evolution)
        df_cleaned = breakdown_date(df)
        df_cleaned = erase_month(df_cleaned)
        time_evolution(df_cleaned)

if __name__ == '__main__':
    main()
