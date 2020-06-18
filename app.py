'''from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key = ""


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:MySql2020!@localhost/workshop-python'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    email = db.Column(db.String(150))

    def __init__(self, name, email):
        self.name = name
        self.email = email


@app.route('/')
def index():
    people = Person.query.all()

    result = []

    for person in people:
        data = {}
        data['id'] = person.id
        data['name'] = person.name
        data['email'] = person.email

        result.append(data)

    return jsonify(result)

    return 'tudo certo'


@app.route('/person', methods=['Post'])
def insert():
    name = request.json['name']
    email = request.json['email']

    person = Person(name, email)
    db.session.add(person)
    db.session.commit()

    return "Pessoa inserida com sucesso"


@app.route('/person/<id>', methods=['GET'])
def get(id):
    person = Person.query.get(id)

    result = {
        'id': person.id,
        'name': person.name,
        'email': person.email
    }

    return jsonify(result)


@app.route('/person', methods=['PUT'])
def update():
    id = request.json['id']
    person = Person.query.get(id)

    person.name = request.json['name']
    person.email = request.json['email']

    db.session.commit()

    return "Pessoa atualizada com sucesso!"


@app.route('/person/<id>', methods=['DELETE'])
def delete(id):
    person = Person.query.get(id)

    db.session.delete(person)
    db.session.commit()

    return "Pessoa excluída com sucesso!"'''