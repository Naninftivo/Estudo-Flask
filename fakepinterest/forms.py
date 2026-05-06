# criar os formulários
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, length, ValidationError
from fakepinterest.models import Usuario

class FormLogin(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    senha = PasswordField("Senha", validators=[DataRequired()])
    butao_confirmacao = SubmitField("Fazer cogin")

class FormCriarConta(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    username = StringField("Nome de usuário", validators=[DataRequired()])
    senha = PasswordField("Senha", validators=[DataRequired(), length(6,20)])
    confirmacao_senha = PasswordField("Confirmar senha", validators=[DataRequired(), EqualTo("senha")])
    butao_confirmacao = SubmitField("Criar conta")

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            return ValidationError("E-mail já cadastrado, faça login para continuar")