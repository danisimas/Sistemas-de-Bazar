import random
import csv
import requests
from faker import Faker
import json 

fake = Faker()

def read_ceps_from_csv(file_path):
    with open(file_path, 'r', newline='', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file, delimiter=',', quotechar='"')
        next(reader)  # Pular a primeira linha (cabeçalho)
        ceps = [row[0] for row in reader]
    return ceps

def get_random_cep_from_list(ceps):
    return random.choice(ceps)
    
def generate_valid_postcode(ceps_list):
    valid_postcode = ""

    while not valid_postcode:
        random_postcode = get_random_cep_from_list(ceps_list)
        response = requests.get(f'https://brasilapi.com.br/api/cep/v2/{random_postcode}')
        
        try:
            response_data = response.json()
        except json.JSONDecodeError:
            continue  # Skip the current iteration and try again with another random postcode

        if response.status_code == 200:
            print(response_data)
            valid_postcode = random_postcode

    return valid_postcode


ceps_list = read_ceps_from_csv('ceps - ceps.csv')


def get_lat_lng_by_cep(cep):
    try:
        response = requests.get(f'https://brasilapi.com.br/api/cep/v2/{cep}')
        data = response.json()
        return data['location']['coordinates']['latitude'], data['location']['coordinates']['longitude']
    except:
        return '?', '?'


def get_address_by_cep(cep):
    try:
        response = requests.get(f'https://brasilapi.com.br/api/cep/v2/{cep}')
        data = response.json()
        return f"{data['street']}, {data['neighborhood']}, {data['city']}, {data['state']}"
    except:
        return "CEP não encontrado na base dos Correios"

def write_csv_row(writer, name, cep, lat, lon, address, product_list=None):
    if product_list is not None:
        writer.writerow([name, cep, lat, lon, address, product_list])
    else:
        writer.writerow([name, cep, lat, lon, address])

# Create CSV file for Users
unique_cep_users = set()
with open('usuarios.csv', mode='w', newline='', encoding='utf-8') as usuarios_file:
    usuarios_writer = csv.writer(usuarios_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    usuarios_writer.writerow(['Nome Usuário', 'CEP Usuário', 'Latitude', 'Longitude', 'Endereço'])

    for i in range(500):
        nome_usuario = fake.name()
        cep_usuario = generate_valid_postcode(ceps_list)

        while cep_usuario in unique_cep_users:
            cep_usuario = generate_valid_postcode(ceps_list)
        unique_cep_users.add(cep_usuario)

        lat_usuario, lon_usuario = get_lat_lng_by_cep(cep_usuario)
        endereco_usuario = get_address_by_cep(cep_usuario)

        write_csv_row(usuarios_writer, nome_usuario, cep_usuario, lat_usuario, lon_usuario, endereco_usuario)


# Auxiliary functions
def generate_random_product_name():
    return f"{fake.color_name()} {fake.random_element(['Shirt', 'Lego', 'Barbie', 'Hot Wheels', 'Nerf', 'Fisher-Price', 'Play-Doh', 'Transformers', 'My Little Pony', 'Monopoly', 'Beyblade', 'Pants', 'Shoes', 'Hat', 'Bag', 'Glasses', 'Socks', 'Tie', 'Belt', 'Watch', 'Scarf', 'Jacket', 'Dress', 'Skirt', 'Shorts', 'Action Figure', 'Doll', 'Board Game', 'Card Game', 'Building Blocks', 'Puzzle', 'Remote Control Car', 'Train Set', 'Bicycle', 'Scooter'])}"

categorias = [f"Roupas {sexo} {idade}" for sexo in ['Femininas', 'Masculinas'] for idade in ['Adulto', 'Infantil']]
categorias += ['Acessórios', 'Sapatos', 'Bolsas', 'Livros', 'Brinquedos', 'Eletrônicos', 'Móveis', 'Decoração', 'Utensílios domésticos']

categorias += [f'Brinquedos {tipo}' for tipo in ['Ação', 'Bonecas', 'Veículos', 'Jogos de Tabuleiro', 'Blocos de Montar']]
categorias += ['Marcas de Brinquedos', 'Jogos Eletrônicos']

# Create CSV file for Bazaars
with open('bazares.csv', mode='w', newline='', encoding='utf-8') as bazares_file:
    bazares_writer = csv.writer(bazares_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    bazares_writer.writerow(['Nome Bazar', 'CEP Bazar', 'Latitude', 'Longitude', 'Endereço', 'Lista de Produtos'])

    for i in range(50):
        nome_bazar = fake.company()
        cep_bazar = generate_valid_postcode(ceps_list)

        lat_bazar, lon_bazar = get_lat_lng_by_cep(cep_bazar)
        endereco_bazar = get_address_by_cep(cep_bazar)

        lista_produtos = ', '.join([f"{random.choice(categorias)}: {generate_random_product_name()} (Quantidade: {random.randint(1, 20)})" for _ in range(random.randint(3, 6))])

        write_csv_row(bazares_writer, nome_bazar, cep_bazar, lat_bazar, lon_bazar, endereco_bazar, lista_produtos)