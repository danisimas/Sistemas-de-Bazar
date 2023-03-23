Train = [{
    'Bazar': 'Ludus',
    'Nota_Atendimento': 6,
    'Nota_Organização': 10,
    'Nota_Aparência': 5,
    'Nota_Variedade': 10,
    'Nota_Forma_Pagamento': 7
}, {
    'Bazar': 'Ctic',
    'Nota_Atendimento': 4,
    'Nota_Organização': 5,
    'Nota_Aparência': 3,
    'Nota_Variedade': 1,
    'Nota_Forma_Pagamento': 7
}, {
    'Bazar': 'Stem',
    'Nota_Atendimento': 3,
    'Nota_Organização': 10,
    'Nota_Aparência': 7,
    'Nota_Variedade': 2,
    'Nota_Forma_Pagamento': 7
}, {
    'Bazar': 'Calidus',
    'Nota_Atendimento': 10,
    'Nota_Organização': 10,
    'Nota_Aparência': 10,
    'Nota_Variedade': 10,
    'Nota_Forma_Pagamento': 7
}, {
    'Bazar': 'Baja',
    'Nota_Atendimento': 5,
    'Nota_Organização': 7,
    'Nota_Aparência': 6,
    'Nota_Variedade': 4,
    'Nota_Forma_Pagamento': 7
}, {
    'Bazar': 'Ocean',
    'Nota_Atendimento': 9,
    'Nota_Organização': 10,
    'Nota_Aparência': 3,
    'Nota_Variedade': 6,
    'Nota_Forma_Pagamento': 7
}]

text = {
    'Bazar': 'Teste',
    'Nota_Atendimento': 6,
    'Nota_Organização': 1,
    'Nota_Aparência': 9,
    'Nota_Variedade': 2,
    'Nota_Forma_Pagamento': 7
}


def dist_eucli(usuario1, usuario2):
    dist = 0
    dist = pow(usuario1['Nota_Atendimento'] - usuario2['Nota_Atendimento'], 2)
    dist += pow(usuario1['Nota_Organização'] - usuario2['Nota_Organização'], 2)
    dist += pow(usuario1['Nota_Aparência'] - usuario2['Nota_Aparência'], 2)
    dist += pow(usuario1['Nota_Variedade'] - usuario2['Nota_Variedade'], 2)
    dist += pow(
        usuario1['Nota_Forma_Pagamento'] - usuario2['Nota_Forma_Pagamento'], 2)
    return dist**0.5


def vizinho_proximo(data, resposta, k):
    vizinhos = []
    for bazar in data:
        vizinhos.append((bazar, dist_eucli(bazar, resposta)))
    vizinhos.sort(key=lambda tup: tup[1])
    topo = vizinhos[0:k]
    return topo


print(vizinho_proximo(Train, text, 1))