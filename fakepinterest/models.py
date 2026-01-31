#criar a estrutura do banco de dados
from fakepinterest import database
from datetime import datetime

class Usuario(database.Model): #tabela de usuários
    id = database.Column(database.Integer, primary_key=True) #identificador único do usuário
    username = database.Column(database.String, nullable=False) #nome de usuário 
    email = database.Column(database.String, unique=True, nullable=False) #email do usuário
    senha = database.Column(database.String, nullable=False) #senha do usuário 
    fotos = database.relationship('Foto', backref='usuario', lazy=True) #relacionamento com a tabela Foto

class Foto(database.Model): #tabela de fotos
    id = database.Column(database.Integer, primary_key=True) #identificador único da foto
    imagem = database.Column(database.String, default='default.png') #caminho da imagem
    data_criacao = database.Column(database.DateTime, nullable=False, default=datetime.utcnow()) #data de criação da foto
    id_usuario = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False) #chave estrangeira para o usuário que postou a foto
