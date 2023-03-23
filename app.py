from flask import Flask, render_template, url_for, request, redirect, flash, session
import requests
import time
from recomendations import recomendar_itens, recomendar_itens_com_palavra


app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Dicionário para armazenar dados de usuários registrados
registered_users = {}


@app.route("/")
def index():
    return render_template("index.html")


@app.route('/register')
def registerPage():
    return render_template("register.html")


def is_valid_cep(cep):
    response = requests.get(f"https://brasilapi.com.br/api/cep/v2/{cep}")
    if response.json().get("erro", False):
        return None
    else:
        cep_info = response.json()
        return {
            "cep": cep_info["cep"],
            "latitude": cep_info['location']['coordinates']['latitude'],
            "longitude": cep_info['location']['coordinates']['longitude']
        }


@app.route('/register_user', methods=['POST'])
def register_user():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    cep = request.form['cep']
    username = request.form['username']
    password = request.form['password']
    confirm_password = request.form['confirm_password']
    if password != confirm_password:
        flash("As senhas não são iguais.")

        return redirect(url_for("registerPage"))

    cep_info = is_valid_cep(cep)
    if not cep_info:
        flash("CEP inválido.")

        return redirect(url_for("registerPage"))

    registered_users[username] = {
        "username": username,
        "first_name": first_name,
        "last_name": last_name,
        "cep": cep_info["cep"],
        "latitude": cep_info["latitude"],
        "longitude": cep_info["longitude"],
        "password": password
    }

    print("Registration" + str(registered_users))

    flash("Registro concluído com sucesso.")
    time.sleep(1)
    return redirect(url_for("loginPage"))




@app.route('/login')
def loginPage():
    return render_template("login.html")


@app.route("/ufinds", methods=['GET', 'POST'])
def ufinds():
    if 'username' not in session:
        flash('Usuário não cadastrado.', 'error')
        return redirect('/login')
    username = session['username']
    user = registered_users.get(username)

    if not user:
        flash('Usuário não cadastrado.', 'error')
        return redirect('/login')

    search_applied = False
    search = None
    if request.method == 'POST':
        search = request.form.get("search")
        if search:
            search_applied = True
            bazares_recomendados = recomendar_itens_com_palavra(user["latitude"], user["longitude"], search)
        else:
            search_applied = False
            bazares_recomendados = recomendar_itens(user["latitude"], user["longitude"])
    else:
        bazares_recomendados = recomendar_itens(user["latitude"], user["longitude"])

    return render_template("ufinds.html", first_name=user["first_name"], last_name=user["last_name"], cep=user["cep"], latitude=user["latitude"], longitude=user["longitude"], bazares=bazares_recomendados, search_applied=search_applied)



@app.route("/login", methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username in registered_users and registered_users[username]['password'] == password:
        session['username'] = username
        flash('Login bem-sucedido. Redirecionando', 'success')
        return redirect('/ufinds')
    else:
        flash('Usuário não cadastrado ou senha incorreta.', 'error')

        return redirect('/login')



if __name__ == "__main__":
    app.run(debug=True)