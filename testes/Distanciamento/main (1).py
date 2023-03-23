import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# definir dados de exemplo
itens = {
    'Item 1': {
        'descricao': 'Este é o Item 1. Possui um design moderno e elegante.',
        'palavras_chave': 'item, moderno, elegante, design',
        'latitude': -23.567778,
        'longitude': -46.648889
    },
    'Item 2': {
        'descricao':
        'Este é o Item 2. Possui um design clássico e sofisticado.',
        'palavras_chave': 'item, clássico, sofisticado, design',
        'latitude': -23.568889,
        'longitude': -46.649444
    },
    'Item 3': {
        'descricao':
        'Este é o Item 3. Possui um design simples e minimalista.',
        'palavras_chave': 'item, simples, minimalista, design',
        'latitude': -23.570000,
        'longitude': -46.649722
    }
}


# função para recomendação de itens
def recomendar_itens(palavras_chave, latitude, longitude):
    # criar vetor de palavras-chave do usuário
    palavras_chave_usuario = palavras_chave.split(',')

    # criar matriz de vetores de palavras-chave dos itens
    vetores_palavras_chave = []
    for item in itens:
        palavras_chave_item = itens[item]['palavras_chave'].split(',')
        vetor = np.zeros(len(palavras_chave_usuario))
        for i, palavra_chave in enumerate(palavras_chave_usuario):
            if palavra_chave in palavras_chave_item:
                vetor[i] = 1
        vetores_palavras_chave.append(vetor)
    matriz_palavras_chave = np.vstack(vetores_palavras_chave)

    # calcular similaridade dos cossenos entre vetor do usuário e vetores dos itens
    vetor_usuario = np.ones(len(palavras_chave_usuario))
    similaridade = cosine_similarity(matriz_palavras_chave,
                                     vetor_usuario.reshape(1, -1))

    # ordenar itens pela similaridade dos cossenos e pela distância do usuário
    itens_recomendados = []
    for i, item in enumerate(itens):
        distancia = np.sqrt((latitude - itens[item]['latitude'])**2 +
                            (longitude - itens[item]['longitude'])**2)
        itens_recomendados.append((item, similaridade[i][0], distancia))
    itens_recomendados = sorted(itens_recomendados,
                                key=lambda x: (x[1], -x[2]),
                                reverse=True)

    # retornar os 2 itens mais similares ao usuário
    return [item[0] for item in itens_recomendados[:1]]


# exemplo de uso da função
palavras_chave = input('Digite as palavras-chave separadas por vírgulas: ')
latitude = float(input('Digite a latitude do usuário: '))
longitude = float(input('Digite a longitude do usuário: '))
itens_recomendados = recomendar_itens(palavras_chave, latitude, longitude)
print('Itens recomendados:', itens_recomendados)
