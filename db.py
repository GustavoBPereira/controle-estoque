from config import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)


class Estoque(db.Model):
    __tablename_ = 'produtos'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.Text, unique=True)
    valor_compra = db.Column(db.Text)
    valor_venda = db.Column(db.Text)
    quantidade_estoque = db.Column(db.Text)
    quantidade_ideal = db.Column(db.Text)
