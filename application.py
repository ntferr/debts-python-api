from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = ""

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:MySql2020!@localhost/workshop-python'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Divida(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_pessoa = db.Column(db.Integer, db.ForeignKey('pessoa.id'), nullable=False)
    valor = db.Column(db.Float)
    flag = db.Column(db.Boolean)

    def __init__(self, divida):
        self.id_pessoa = divida['id_pessoa']
        self.valor = divida['valor']
        self.flag = divida['flag']

class Pessoa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150))
    email = db.Column(db.String(150))
    #dividas = db.relationship('Dividas', backref='Pessoa')

    def __init__(self, pessoa):
        self.nome = pessoa['nome']
        self.email = pessoa['email']

#------------------------------------

@app.route('/pessoa/<id>', methods=['GET'])
def get_home_pessoa(id):
    result = get_pessoa(id)
    return result

@app.route('/divida/<id>', methods=['GET'])
def get_home_divida(id):
    result = get_divida(id)
    return result

@app.route('/pessoa', methods=['Post'])
def insrt_person():
    insert_pessoa()
    return "Pessoa inserida com sucesso!"

@app.route('/divida', methods=['Post'])
def insrt_divida():
    insert_divida()
    return "Divida inserida com sucesso!"

@app.route('/pessoa/<id>', methods=['PUT'])
def updt_pessoa(id):
    update_pessoa(id)
    return "Pessoa atualizada com sucesso"

@app.route('/divida/<id>', methods=['PUT'])
def updt_divida(id):
    update_divida(id)
    return "Divida atualizada com sucesso"

@app.route('/pessoa/<id>', methods=['DELETE'])
def dlt(id):
    delete(id)
    return "Exclusão de cadastro feita"


#-----------------------------------

def insert_pessoa():
    dados = {}
    dados['nome'] = request.json['name']
    dados['email'] = request.json['email']

    pessoa = Pessoa(dados)

    db.session.add(pessoa)
    db.session.commit()


def insert_divida():
    dados = {}
    dados['id_pessoa'] = request.json['id_pessoa']
    dados['valor'] = request.json['valor']
    dados['flag'] = request.json['flag']

    divida = Divida(dados)

    db.session.add(divida)
    db.session.commit()


def get_pessoa(id):
    pessoa = request.query.get(id)

    result = {
        "id": pessoa.id,
        "name": pessoa.nome,
        "email": pessoa.email
    }
    return jsonify(result)

def get_divida(id):
    divida = request.query.get(id)

    result = {
        "id": divida.id,
        "valor": divida.valor,
        "flag": divida.flag
    }
    return jsonify(result)

def update_pessoa():
    id = request.json['id']
    pessoa = request.query.get(id)

    pessoa.nome = request.json['nome']
    pessoa.email = request.json['email']

    db.session.commit()


def update_divida():
    id = request.json['id']
    divida = request.query.id(id)

    divida.valor = request.json['valor']
    divida.flag = request.json['flag']

    db.session.commit()


def delete(id):
    pessoa = Pessoa.query.get(id)
    divida = Divida.query.filter_by(id_pessoa = pessoa.id).first()

    db.session.delete(pessoa)
    db.session.delete(divida)

    db.session.commit()
