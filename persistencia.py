from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from models.pessoa import Pessoa
from models.divida import Divida


app = Flask(__name__)
app.secret_key = ""

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:MySql2020!@localhost/workshop-python'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

def insert_pessoa(self):
    dados = {}
    dados['nome'] = request.json['name']
    dados['email'] = request.json['email']

    pessoa = Pessoa(dados)

    db.session.add(pessoa)
    db.session.commit()


def insert_divida(self):
    dados = {}
    dados['id_pessoa'] = request.json['id_pessoa']
    dados['valor'] = request.json['valor']
    dados['flag'] = request.json['flag']

    divida = Divida(dados)

    db.session.add(divida)
    db.session.commit()


def get_pessoa(self, id):
    pessoa = request.query.get(id)

    result = {
        "id": pessoa.id,
        "name": pessoa.nome,
        "email": pessoa.email
    }
    return jsonify(result)

def get_divida(self, id):
    divida = request.query.get(id)

    result = {
        "id": divida.id,
        "valor": divida.valor,
        "flag": divida.flag
    }
    return jsonify(result)

def update_pessoa(self):
    id = request.json['id']
    pessoa = request.query.get(id)

    pessoa.nome = request.json['nome']
    pessoa.email = request.json['email']

    db.session.commit()


def update_divida(self):
    id = request.json['id']
    divida = request.query.id(id)

    divida.valor = request.json['valor']
    divida.flag = request.json['flag']

    db.session.commit()


def delete(self, id):
    pessoa = Pessoa.query.get(id)
    divida = Divida.query.filter_by(id_pessoa = pessoa.id).first()

    db.session.delete(pessoa)
    db.session.delete(divida)

    db.session.commit()


