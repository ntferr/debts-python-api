from persistencia import db

class Pessoa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150))
    email = db.Column(db.String(150))
    dividas = db.relationship('Dividas', backref='Pessoa')

    def __init__(self, pessoa):
        self.nome = pessoa['nome']
        self.email = pessoa['email']
