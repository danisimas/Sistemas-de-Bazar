import pandas as pd
from geopy import distance

def recomendar_itens(latitude, longitude):
    latitude = float(latitude)
    longitude = float(longitude)
    user_location = (latitude, longitude)

    df = pd.read_csv('bazares.csv')  # Supondo que o arquivo CSV se chama 'bazares.csv'
    df['Latitude'] = pd.to_numeric(df['Latitude'], errors='coerce')
    df['Longitude'] = pd.to_numeric(df['Longitude'], errors='coerce')

    # Remover linhas com valores inválidos de latitude e longitude
    df.dropna(subset=['Latitude', 'Longitude'], inplace=True)

    # Calcular a distância Haversine para cada bazar
    df['distancia'] = df.apply(lambda row: distance.distance(user_location, (row['Latitude'], row['Longitude'])).m, axis=1)

    # Ordenar os itens pela distância
    df.sort_values(by='distancia', inplace=True)

    # Retornar os 20 itens mais próximos
    return df.head(20)
