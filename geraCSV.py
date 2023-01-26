import csv
import random

# Geração de dados fictícios para o arquivo CSV
data = []
usuarios = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Heidi", "Isabel", "Jack"]
estandes = ["Bolsas da Tina", "Your Soul", "REDUX", "Estande da Leila", "Brechózinho", "Vestidos Incríveis", "Sapatos Fofos", "Acessórios da Moda", "Roupas do Coração", "Tudo de Melhor"]
for i in range(100):
    usuario = random.choice(usuarios)
    estande = random.choice(estandes)
    nota_atendimento = round(random.uniform(1, 5), 1)
    nota_organizacao = round(random.uniform(1, 5), 1)
    nota_aparencia = round(random.uniform(1, 5), 1)
    nota_variedade = round(random.uniform(1, 5), 1)
    nota_forma_pagamento = round(random.uniform(1, 5), 1)
    data.append({"Usuário": usuario, "Estande": estande, "Nota_Atendimento": nota_atendimento, "Nota_Organização": nota_organizacao, "Nota_Aparência": nota_aparencia, "Nota_Variedade": nota_variedade, "Nota_Forma_Pagamento": nota_forma_pagamento})

# Criação do arquivo CSV
with open("dados.csv", "w", newline="") as f:
    fieldnames = ["Usuário", "Estande", "Nota_Atendimento", "Nota_Organização", "Nota_Aparência", "Nota_Variedade", "Nota_Forma_Pagamento"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for d in data:
        writer.writerow(d)

# Carregando o arquivo CSV em um dicionário
data = []
with open("dados.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        data.append(row)

print(data)