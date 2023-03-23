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

def extract_product_words(product_list):
    products = product_list.split(", ")
    product_words = [product.split(" ")[1:] for product in products]
    flattened_words = [word for sublist in product_words for word in sublist]
    return flattened_words

def max_similarity(product_list, target_word):
    product_words = extract_product_words(product_list)
    similarities = [fuzz.token_sort_ratio(target_word, word) for word in product_words]
    return max(similarities)

def recomendar_itens_com_palavra(latitude, longitude, palavra):
    latitude = float(latitude)
    longitude = float(longitude)
    user_location = (latitude, longitude)

    df = pd.read_csv('bazares.csv')
    df['Latitude'] = pd.to_numeric(df['Latitude'], errors='coerce')
    df['Longitude'] = pd.to_numeric(df['Longitude'], errors='coerce')

    df.dropna(subset=['Latitude', 'Longitude'], inplace=True)

    df['distancia'] = df.apply(lambda row: distance.distance(user_location, (row['Latitude'], row['Longitude'])).m, axis=1)
    df['similaridade'] = df['Lista de Produtos'].apply(lambda x: max_similarity(x, palavra))
    df['score'] = (1 - df['distancia'] / df['distancia'].max()) * 0.25 + df['similaridade'] / 100 * 0.75
    df.sort_values(by=['score', 'similaridade'], ascending=[False, False], inplace=True)
    print(df['score'])
    return df.head(20)
