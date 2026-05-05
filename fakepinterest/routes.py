# criar as rotas
from flask import render_template, url_for
from fakepinterest import app

@app.route('/') #Criando rota para o site
def homepage():
    return render_template("homepage.html")

@app.route('/perfil/<nome>')
def perfil(nome):
    return render_template("perfil.html", nome=nome)
