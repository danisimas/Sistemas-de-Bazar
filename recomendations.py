import pandas as pd
from geopy import distance
from fuzzywuzzy import fuzz

def recomendar_itens(latitude, longitude):
    latitude = float(latitude)
    longitude = float(longitude)
    user_location = (latitude, longitude)

    df = pd.read_csv('bazares.csv')
    df['Latitude'] = pd.to_numeric(df['Latitude'], errors='coerce')
    df['Longitude'] = pd.to_numeric(df['Longitude'], errors='coerce')

    df.dropna(subset=['Latitude', 'Longitude'], inplace=True)

    df['distancia'] = df.apply(lambda row: distance.distance(user_location, (row['Latitude'], row['Longitude'])).m, axis=1)
    df.sort_values(by='distancia', inplace=True)

    return df.head(20)

def recomendar_itens_com_palavra(latitude, longitude, palavra):
    latitude = float(latitude)
    longitude = float(longitude)
    user_location = (latitude, longitude)

    df = pd.read_csv('bazares.csv')
    df['Latitude'] = pd.to_numeric(df['Latitude'], errors='coerce')
    df['Longitude'] = pd.to_numeric(df['Longitude'], errors='coerce')

    df.dropna(subset=['Latitude', 'Longitude'], inplace=True)

    df['distancia'] = df.apply(lambda row: distance.distance(user_location, (row['Latitude'], row['Longitude'])).m, axis=1)
    df['similaridade'] = df['Lista de Produtos'].apply(lambda x: fuzz.token_sort_ratio(palavra, x))
    df['score'] = (1 - df['distancia'] / df['distancia'].max()) * 0.5 + df['similaridade'] / 100 * 0.5
    df.sort_values(by='score', ascending=False, inplace=True)

    return df.head(20)
