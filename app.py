from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/register')
def registerPage():
    return render_template("register.html")


@app.route('/login')

def loginPage():
    return render_template("login.html")

@app.route("/login", methods=['POST'])
def login():
    if (request.form['username'] == 'admin' and request.form['password'] == 'admin'):
      return redirect('/ufinds')
    else:
      return redirect('/')


@app.route("/profile")
def profile():
    return render_template("profile.html")

@app.route("/ufinds")
def ufinds():
    return render_template("ufinds.html")

if __name__ == "__main__":
    app.run(debug=True)
