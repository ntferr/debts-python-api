from persistencia import *

@app.router("/pessoa/<id>", methods=["GET"])
def get_home_pessoa(id):
    result = get_pessoa(id)
    return result

@app.router("/divida/<id>", methods=["GET"])
def get_home_divida(id):
    result = get_divida(id)
    return result