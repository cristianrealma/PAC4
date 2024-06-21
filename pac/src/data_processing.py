# src/data_processing.py

import pandas as pd

def read_csv(filepath):
    df = pd.read_csv(filepath)
    print("Les cinc primeres files del DataFrame:")
    print(df.head())
    print("\nInformació del DataFrame:")
    print(df.info())
    return df

def clean_csv(df):
    columns_to_keep = ['month', 'state', 'permit', 'handgun', 'long_gun']
    df_cleaned = df[columns_to_keep]
    print("Noms de les columnes després de la neteja:")
    print(df_cleaned.columns)
    return df_cleaned

def rename_col(df):
    df_renamed = df.rename(columns={'longgun': 'long_gun'})
    print("Noms de les columnes després de canviar el nom:")
    print(df_renamed.columns)
    return df_renamed

def breakdown_date(df):
    df[['year', 'month']] = df['month'].str.split('-', expand=True).astype(int)
    print("Les cinc primeres files després de dividir la columna month:")
    print(df.head())
    return df

def erase_month(df):
    df = df.drop(columns=['month'])
    print("Les cinc primeres files després d'eliminar la columna month:")
    print(df.head())
    print("Noms de les columnes després d'eliminar la columna month:")
    print(df.columns)
    return df

def groupby_state_and_year(df):
    """
    Agrupa el dataframe per estat i any, i calcula els valors acumulats totals per cada grup.

    Parameters:
    df (pd.DataFrame): DataFrame original amb les columnes year i state.

    Returns:
    pd.DataFrame: DataFrame amb les dades agrupades per estat i any.
    """
    df_grouped = df.groupby(['state', 'year']).sum().reset_index()
    return df_grouped

def print_biggest_handguns(df):
    """
    Imprimeix l'estat i l'any amb el nombre més gran de hand_guns.

    Parameters:
    df (pd.DataFrame): DataFrame agrupat per estat i any.

    Returns:
    None
    """
    max_handguns = df.loc[df['handgun'].idxmax()]
    print(f"El nombre més gran de hand_guns es va registrar a l'estat {max_handguns['state']} l'any {max_handguns['year']} amb {max_handguns['handgun']} peticions.")

def print_biggest_longguns(df):
    """
    Imprimeix l'estat i l'any amb el nombre més gran de long_guns.

    Parameters:
    df (pd.DataFrame): DataFrame agrupat per estat i any.

    Returns:
    None
    """
    max_longguns = df.loc[df['long_gun'].idxmax()]
    print(f"El nombre més gran de long_guns es va registrar a l'estat {max_longguns['state']} l'any {max_longguns['year']} amb {max_longguns['long_gun']} peticions.")
