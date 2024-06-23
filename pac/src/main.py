
import argparse
from data_processing import read_csv, clean_csv, rename_col, breakdown_date, erase_month, groupby_state_and_year, print_biggest_handguns, print_biggest_longguns, groupby_state, clean_states, merge_datasets, calculate_relative_values
from visualization import generate_maps

def main():
    # Llegir el dataset inicial
    firearm_data = read_csv('path_to_your_csv_file.csv')
    
    # Netejar i processar el dataset
    firearm_data = clean_csv(firearm_data)
    firearm_data = rename_col(firearm_data)
    firearm_data = breakdown_date(firearm_data)
    firearm_data = erase_month(firearm_data)
    firearm_data = groupby_state_and_year(firearm_data)
    
    # Imprimir el resultat més gran per handguns i longguns
    print_biggest_handguns(firearm_data)
    print_biggest_longguns(firearm_data)
    
    # Agrupar per estat i netejar els estats no necessaris
    state_data = groupby_state(firearm_data)
    state_data = clean_states(state_data)
    
    # Fusionar amb dades poblacionals i calcular valors relatius
    population_data = read_csv('path_to_population_csv_file.csv')
    merged_data = merge_datasets(state_data, population_data)
    relative_data = calculate_relative_values(merged_data)
    
    # Generar els mapes coroplètics
    generate_maps(relative_data)

if __name__ == '__main__':
    main()
