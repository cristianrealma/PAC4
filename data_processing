# src/data_processing.py

import pandas as pd

def read_csv(filepath):
    """
    Llegeix un fitxer CSV des d'una ruta de fitxer i retorna un dataframe de pandas.

    Parameters:
    filepath (str): La ruta del fitxer CSV a llegir.

    Returns:
    pd.DataFrame: DataFrame carregat des del fitxer CSV.

    Mostra per pantalla les cinc primeres files i la informació del DataFrame.
    """
    df = pd.read_csv(filepath)
    print("Les cinc primeres files del DataFrame:")
    print(df.head())
    print("\nInformació del DataFrame:")
    print(df.info())
    return df

def clean_csv(df):
    """
    Neteja el dataset inicial, eliminant totes les columnes excepte les necessàries.

    Parameters:
    df (pd.DataFrame): DataFrame original.

    Returns:
    pd.DataFrame: DataFrame netejat contenint únicament les columnes necessàries.

    Mostra per pantalla el nom de totes les columnes del dataframe.
    """
    columns_to_keep = ['month', 'state', 'permit', 'handgun', 'long_gun']
    df_cleaned = df[columns_to_keep]
    print("Noms de les columnes després de la neteja:")
    print(df_cleaned.columns)
    return df_cleaned

def rename_col(df):
    """
    Canvia el nom de la columna 'longgun' per 'long_gun'.

    Parameters:
    df (pd.DataFrame): DataFrame original.

    Returns:
    pd.DataFrame: DataFrame amb el nom de la columna canviat.

    Mostra per pantalla el nom de totes les columnes del dataframe.
    """
    df_renamed = df.rename(columns={'longgun': 'long_gun'})
    print("Noms de les columnes després de canviar el nom:")
    print(df_renamed.columns)
    return df_renamed

def breakdown_date(df):
    """
    Divideix la informació que hi ha a la columna month creant dues noves columnes: year i month.

    Parameters:
    df (pd.DataFrame): DataFrame original amb la columna month.

    Returns:
    pd.DataFrame: DataFrame amb les columnes year i month separades.

    Mostra per pantalla les cinc primeres files del dataframe resultant.
    """
    df[['year', 'month']] = df['month'].str.split('-', expand=True).astype(int)
    print("Les cinc primeres files després de dividir la columna month:")
    print(df.head())
    return df

def erase_month(df):
    """
    Elimina la columna month del DataFrame.

    Parameters:
    df (pd.DataFrame): DataFrame original amb la columna month.

    Returns:
    pd.DataFrame: DataFrame sense la columna month.

    Mostra per pantalla les cinc primeres files i el nom de totes les columnes del dataframe.
    """
    df = df.drop(columns=['month'])
    print("Les cinc primeres files després d'eliminar la columna month:")
    print(df.head())
    print("Noms de les columnes després d'eliminar la columna month:")
    print(df.columns)
    return df
