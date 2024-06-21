# src/data_processing.py

import pandas as pd
import matplotlib.pyplot as plt

# ... altres funcions ...

def time_evolution(df):
    """
    Crea un gràfic que mostra l'evolució temporal de permit, hand_gun i long_gun per any.

    Parameters:
    df (pd.DataFrame): DataFrame amb les dades a agrupar per any.

    Returns:
    None
    """
    df_grouped = df.groupby('year').sum().reset_index()

    plt.figure(figsize=(12, 6))
    plt.plot(df_grouped['year'], df_grouped['permit'], label='Permit', marker='o')
    plt.plot(df_grouped['year'], df_grouped['handgun'], label='Handgun', marker='o')
    plt.plot(df_grouped['year'], df_grouped['long_gun'], label='Long Gun', marker='o')

    plt.xlabel('Year')
    plt.ylabel('Number of Checks')
    plt.title('Time Evolution of Firearm Background Checks in the USA')
    plt.legend()
    plt.grid(True)
    plt.show()
