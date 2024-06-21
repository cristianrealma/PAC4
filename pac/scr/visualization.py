
import folium
import pandas as pd
import json
import io
from PIL import Image
from selenium import webdriver

def create_choropleth(data, column, name, file_name):
    """
    Crea un mapa coroplètic i el guarda com a imatge PNG.
    
    Args:
        data (pd.DataFrame): DataFrame amb les dades.
        column (str): Columna que volem representar.
        name (str): Nom per a la llegenda del mapa.
        file_name (str): Nom del fitxer per guardar el mapa com a imatge.
    """
    with open('path_to_us_states_json_file.json') as f:
        geo_json_data = json.load(f)

    m = folium.Map(location=[37.8, -96], zoom_start=4)

    folium.Choropleth(
        geo_data=geo_json_data,
        name='choropleth',
        data=data,
        columns=['state', column],
        key_on='feature.id',
        fill_color='YlGn',
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name=name
    ).add_to(m)

    # Guardar el mapa com a HTML
    map_path = f'{file_name}.html'
    m.save(map_path)
    
    # Utilitzar selenium per capturar una imatge del mapa
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.get(f'file://{map_path}')
    
    img_data = driver.get_screenshot_as_png()
    img = Image.open(io.BytesIO(img_data))
    img.save(f'{file_name}.png')
    driver.quit()
    
def generate_maps(df):
    """
    Genera els mapes coroplètics per permit_perc, handgun_perc i longgun_perc.
    
    Args:
        df (pd.DataFrame): DataFrame amb les dades.
    """
    create_choropleth(df, 'permit_perc', 'Percentage of Permits', 'permit_perc_map')
    create_choropleth(df, 'handgun_perc', 'Percentage of Handguns', 'handgun_perc_map')
    create_choropleth(df, 'longgun_perc', 'Percentage of Long Guns', 'longgun_perc_map')
