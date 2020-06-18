from persistencia import db

class Divida(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_pessoa = db.Column(db.Integer, db.ForeignKey('pessoa.id'), nullable=False)
    valor = db.Column(db.Double)
    flag = db.Column(db.Bool)

    def __init__(self, divida):
        self.id_pessoa = divida['id_pessoa']
        self.valor = divida['valor']
        self.flag = divida['flag']