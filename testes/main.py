import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from geopy.distance import geodesic

# Carrega o arquivo CSV com os dados do bazar
df = pd.read_csv('bazar.csv')

# Solicita as palavras-chave e a localização do usuário
palavras_chave = input("Digite algumas palavras-chave separadas por vírgula: ").split(',')
latitude = float(input("Digite a latitude da sua localização: "))
longitude = float(input("Digite a longitude da sua localização: "))

# Calcula a distância entre a localização do usuário e a localização de cada bazar
def calcular_distancia(row):
    bazar_latitude = row['Latitude']
    bazar_longitude = row['Longitude']
    bazar_localizacao = (bazar_latitude, bazar_longitude)
    return geodesic((latitude, longitude), bazar_localizacao).km

df['Distancia'] = df.apply(calcular_distancia, axis=1)

# Normaliza a distância entre 0 e 1
df['Distancia'] = 1 - (df['Distancia'] - df['Distancia'].min()) / (df['Distancia'].max() - df['Distancia'].min())

# Aplica o TF-IDF nas descrições dos itens do bazar
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['Descricao'])

# Calcula a similaridade do cosseno entre as descrições dos itens e as palavras-chave fornecidas pelo usuário
palavras_chave_matrix = tfidf.transform(palavras_chave)
similaridades = cosine_similarity(tfidf_matrix, palavras_chave_matrix)

# Adiciona as similaridades na coluna 'Similaridade'
df['Similaridade'] = similaridades

# Filtra os itens com maior similaridade e maior distância normalizada
recomendacoes = df[(df['Similaridade'] > 0.5) & (df['Distancia'] > 0.5)]

# Imprime as recomendações
print(recomendacoes[['Nome', 'Descricao', 'Latitude', 'Longitude']])
