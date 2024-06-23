
import pandas as pd
import matplotlib.pyplot as plt

# ... altres funcions ...

def groupby_state(df):
    """
    Agrupa el dataframe per estat i calcula els valors totals.

    Parameters:
    df (pd.DataFrame): DataFrame amb les dades a agrupar per estat i any.

    Returns:
    pd.DataFrame: DataFrame amb els valors agrupats per estat.
    """
    df_grouped = df.groupby('state').sum().reset_index()
    print(df_grouped.head())
    return df_grouped

def clean_states(df):
    """
    Elimina els estats Guam, Mariana Islands, Puerto Rico i Virgin Islands del dataframe.

    Parameters:
    df (pd.DataFrame): DataFrame amb les dades agrupades per estat.

    Returns:
    pd.DataFrame: DataFrame sense els estats Guam, Mariana Islands, Puerto Rico i Virgin Islands.
    """
    states_to_remove = ['Guam', 'Mariana Islands', 'Puerto Rico', 'Virgin Islands']
    df_cleaned = df[~df['state'].isin(states_to_remove)]
    print(f"Nombre d'estats diferents: {df_cleaned['state'].nunique()}")
    return df_cleaned

def merge_datasets(df1, df2):
    """
    Fusiona dos dataframes pel nom de l'estat.

    Parameters:
    df1 (pd.DataFrame): DataFrame amb les dades agrupades per estat.
    df2 (pd.DataFrame): DataFrame amb les dades poblacionals.

    Returns:
    pd.DataFrame: DataFrame resultant de fusionar les dades.
    """
    df_merged = pd.merge(df1, df2, how='inner', left_on='state', right_on='state')
    print(df_merged.head())
    return df_merged

def calculate_relative_values(df):
    """
    Calcula els valors relatius per a permit, handgun i long_gun.

    Parameters:
    df (pd.DataFrame): DataFrame amb les dades agrupades per estat i població.

    Returns:
    pd.DataFrame: DataFrame amb les noves columnes de valors relatius.
    """
    df['permit_perc'] = (df['permit'] * 100) / df['pop_2014']
    df['handgun_perc'] = (df['handgun'] * 100) / df['pop_2014']
    df['longgun_perc'] = (df['long_gun'] * 100) / df['pop_2014']
    return df

def analyze_data(df):
    """
    Analitza les dades i realitza diverses operacions.

    Parameters:
    df (pd.DataFrame): DataFrame amb els valors relatius calculats.

    Returns:
    None
    """
    permit_mean = round(df['permit_perc'].mean(), 2)
    print(f"Mitjana de permits: {permit_mean}")

    kentucky_data = df[df['state'] == 'Kentucky']
    print("Informació relativa a l'estat de Kentucky:")
    print(kentucky_data)

    df.loc[df['state'] == 'Kentucky', 'permit_perc'] = permit_mean

    new_permit_mean = round(df['permit_perc'].mean(), 2)
    print(f"Nova mitjana de permits: {new_permit_mean}")

    return df
