from flask import Flask, jsonify, request
import jwt

app = Flask(__name__)

# configuracion de clave secreta 
app.config['SECRET_KEY'] = 'c61ba9e82756f59324f4e7e0c8f5d7e9'

def autenticar():
    token = request.json['token']
    payload = verificar_token(token)
    if payload is not None:

        usuario_id = payload['sub']
        email = payload['email']
        companies = payload['companies']

        for company in companies:
            name = company.get('name')
            if not name or len(name) < 3: # no se cual validacion de nombre utilizar 
                raise ValueError('El campo "name" es inválido')
            role = company.get('role')
            if not role or role not in ['admin', 'user']:
                raise ValueError('El campo "role" es inválido')
            status = company.get('status')
            if not status or status not in ['active', 'inactive']:
                raise ValueError('El campo "status" es inválido')
            
        return 'Autenticación exitosa'
    else:
        return 'Token invalido'

def verificar_token(token):
    try:
        payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        return None  # El token ha expirado
    except jwt.InvalidTokenError:
        return None  # El token no es válido
    

        





# Ejemplo de datos
products = [
    {"id": 1, "name": "Producto 1", "description": "Descripción del producto 1", "price": 10.0},
    {"id": 2, "name": "Producto 2", "description": "Descripción del producto 2", "price": 20.0},
    {"id": 3, "name": "Producto 3", "description": "Descripción del producto 3", "price": 30.0},
]

# Endpoints
@app.route("/products", methods=["GET"])

def get_products():
    return jsonify(products)

@app.route("/products/<int:product_id>", methods=["GET"])
def get_product(product_id):
    product = next((p for p in products if p["id"] == product_id), None)
    if product:
        return jsonify(product)
    else:
        return "Producto no encontrado", 404

@app.route("/products", methods=["POST"])
def create_product():
    new_product = {
        "id": len(products) + 1,
        "name": request.json["name"],
        "description": request.json.get("description", ""),
        "price": request.json["price"],
    }
    products.append(new_product)
    return jsonify(new_product), 201

@app.route("/products/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    product = next((p for p in products if p["id"] == product_id), None)
    if product:
        product["name"] = request.json["name"]
        product["description"] = request.json.get("description", "")
        product["price"] = request.json["price"]
        return jsonify(product)
    else:
        return "Producto no encontrado", 404

@app.route("/products/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    product = next((p for p in products if p["id"] == product_id), None)
    if product:
        products.remove(product)
        return "", 204
    else:
        return "Producto no encontrado", 404

# Ejecutar el servidor
if __name__ == "__main__":
    app.run(debug=True)

