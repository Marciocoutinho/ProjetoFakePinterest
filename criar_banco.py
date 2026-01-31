from fakepinterest import database, app
from fakepinterest.models import Usuario, Foto

#criar o banco de dados
with app.app_context():
    database.create_all()