import csv
import random

# Geração de dados fictícios para o arquivo CSV
data = []
usuarios = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Heidi", "Isabel", "Jack"]
estandes = ["Bolsas da Tina", "Your Soul", "REDUX", "Estande da Leila", "Brechozinho", "Vestidos Incriveis", "Sapatos Fofos", "Acessorios da Moda", "Roupas do Coracao", "Tudo de Melhor"]
for i in range(100):
    usuario = random.choice(usuarios)
    estande = random.choice(estandes)
    nota_atendimento = round(random.uniform(1, 5), 1)
    nota_organizacao = round(random.uniform(1, 5), 1)
    nota_aparencia = round(random.uniform(1, 5), 1)
    nota_variedade = round(random.uniform(1, 5), 1)
    nota_forma_pagamento = round(random.uniform(1, 5), 1)
    data.append({"Usuario": usuario, "Estande": estande, "Nota_Atendimento": nota_atendimento, "Nota_Organizacao": nota_organizacao, "Nota_Aparencia": nota_aparencia, "Nota_Variedade": nota_variedade, "Nota_Forma_Pagamento": nota_forma_pagamento})

# Criação do arquivo CSV
with open("dados.csv", "w", newline="") as f:
    fieldnames = ["Usuario", "Estande", "Nota_Atendimento", "Nota_Organizacao", "Nota_Aparencia", "Nota_Variedade", "Nota_Forma_Pagamento"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for d in data:
        writer.writerow(d)


def gera_dici(filepath):
# Carregando o arquivo CSV em um dicionário
    data = []
    with open(filepath) as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)
        return data

print(data)