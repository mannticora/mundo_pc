from flask import Flask, jsonify, request

app = Flask(__name__)

# Ruta principal
@app.route('/')
def home():
    return jsonify({"mensaje": "Bienvenido a mi API en Flask"})

# Ruta para obtener datos (GET)
@app.route('/api/saludo/<nombre>', methods=['GET'])
def saludo(nombre):
    return jsonify({"saludo": f"Hola, {nombre}!"})

# Ruta para enviar datos (POST)
@app.route('/api/sumar', methods=['POST'])
def sumar():
    datos = request.get_json()
    a = datos.get('a', 0)
    b = datos.get('b', 0)
    resultado = a + b
    return jsonify({"resultado": resultado})

if __name__ == '__main__':
    app.run(debug=True)
