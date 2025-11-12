from flask import Flask, jsonify, request

app = Flask(__name__)

# Ruta raíz
@app.route('/')
def home():
    return jsonify({"message": "Bienvenido a mi API en Python 🚀"})

# Ruta GET para obtener datos
@app.route('/saludo/<nombre>', methods=['GET'])
def saludar(nombre):
    return jsonify({"saludo": f"Hola, {nombre}!"})

# Ruta POST para recibir datos
@app.route('/sumar', methods=['POST'])
def sumar():
    data = request.get_json()
    x = data.get('x')
    y = data.get('y')
    resultado = x + y
    return jsonify({"resultado": resultado})

if __name__ == '__main__':
    app.run(debug=True)
