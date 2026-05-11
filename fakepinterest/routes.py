# criar as rotas
from flask import render_template, url_for
from fakepinterest import app
from flask_login import login_required
from fakepinterest.forms import FormLogin, FormCriarConta

@app.route('/', methods=['GET', 'POST']) #Criando rota para o site
def homepage():
    formlogin = FormLogin()
    return render_template("homepage.html", form=formlogin)


@app.route("/criar-conta")
def criarconta():
    formcriarconta = FormCriarConta()
    return render_template("criarconta.html", form=formcriarconta)

@app.route('/perfil/<nome>')
@login_required
def perfil(nome):
    return render_template("perfil.html", nome=nome)
