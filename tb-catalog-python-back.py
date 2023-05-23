from flask import Flask, jsonify, request
import jwt

app = Flask(__name__)

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

