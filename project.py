
import pandas as pd

data = pd.read_csv("dados.csv").to_dict('records')

text = {
    'Nome': 'Teste',
    'Estande': 'Teste',
    'Nota_Atendimento':2.0,
    'Nota_Organizacao': 1.0,
    'Nota_Aparencia': 2.0,
    'Nota_Variedade': 2.0,
    'Nota_Forma_Pagamento': 2.0
}


def dist_eucli(usuario1, usuario2):
    dist = 0
    dist = pow(usuario1['Nota_Atendimento'] - usuario2['Nota_Atendimento'], 2)
    dist += pow(usuario1['Nota_Organizacao'] - usuario2['Nota_Organizacao'], 2)
    dist += pow(usuario1['Nota_Aparencia'] - usuario2['Nota_Aparencia'], 2)
    dist += pow(usuario1['Nota_Variedade'] - usuario2['Nota_Variedade'], 2)
    dist += pow(usuario1['Nota_Forma_Pagamento'] - usuario2['Nota_Forma_Pagamento'], 2)
    return dist**0.5


def vizinho_proximo(data, resposta, k):
    vizinhos = []
    for bazar in data:
        vizinhos.append((bazar, dist_eucli(bazar, resposta)))
    vizinhos.sort(key=lambda tup: tup[1])
    topo = vizinhos[0:k]
    return topo


print(vizinho_proximo(data, text, 1))
