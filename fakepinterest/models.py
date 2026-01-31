# criar a estrutura do banco de dados
from fakepinterest import database, login_manager
from datetime import datetime
from flask_login import UserMixin


@login_manager.user_loader
def load_user(id_usuario):
    return Usuario.query.get(int(id_usuario))


class Usuario(database.Model, UserMixin):  # tabela de usuários
    # identificador único do usuário
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(
        database.String, nullable=False)  # nome de usuário
    email = database.Column(database.String, unique=True,
                            nullable=False)  # email do usuário
    senha = database.Column(
        database.String, nullable=False)  # senha do usuário
    # relacionamento com a tabela Foto
    fotos = database.relationship('Foto', backref='usuario', lazy=True)


class Foto(database.Model):  # tabela de fotos
    # identificador único da foto
    id = database.Column(database.Integer, primary_key=True)
    imagem = database.Column(
        database.String, default='default.png')  # caminho da imagem
    data_criacao = database.Column(
        database.DateTime, nullable=False, default=datetime.utcnow)  # data de criação da foto
    id_usuario = database.Column(database.Integer, database.ForeignKey(
        'usuario.id'), nullable=False)  # chave estrangeira para o usuário que postou a foto
