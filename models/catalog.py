#estructura de datos definicion de catalogo
import pymongo
from pymongo import MongoClient

# Configuración de la conexión a MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['mi_basededatos']  # Reemplaza 'mi_basededatos' por el nombre de tu base de datos

# Obtención de las colecciones
catalogs_collection = db['Catalogs']
products_collection = db['Products']
attributes_collection = db['ProductAttributes']

# Ejemplo de inserción de un catálogo
catalog_data = {
    'id': '1',
    'name': 'Mi catálogo',
    'company_nit': '123456789',  # ID de la compañía a la que pertenece el catálogo
    'created_at': datetime.datetime.now(),
    'updated_at': datetime.datetime.now()
}
catalogs_collection.insert_one(catalog_data)

# Ejemplo de inserción de un producto
product_data = {
    'id': '1',
    'catalog_id': '1',  # ID del catálogo al que pertenece el producto
    'name': 'Mi producto',
    'description': 'Descripción del producto',
    'price': 9.99,
    'created_at': datetime.datetime.now(),
    'updated_at': datetime.datetime.now()
}
products_collection.insert_one(product_data)

# Ejemplo de inserción de un atributo de producto
attribute_data = {
    'id': '1',
    'product_id': '1',  # ID del producto al que pertenece el atributo
    'attribute_name': 'Color',
    'attribute_value': 'Rojo',
    'created_at': datetime.datetime.now(),
    'updated_at': datetime.datetime.now()
}
attributes_collection.insert_one(attribute_data)

# Ejemplo de consulta de catálogos por compañía
company_nit = '123456789'  # NIT de la compañía
query = {'company_nit': company_nit}
result = catalogs_collection.find(query)
for catalog in result:
    print(catalog)

# Ejemplo de actualización de un producto
product_id = '1'  # ID del producto a actualizar
new_name = 'Nuevo nombre'
update_query = {'id': product_id}
new_values = {'$set': {'name': new_name}}
products_collection.update_one(update_query, new_values)

# Ejemplo de eliminación de un catálogo
catalog_id = '1'  # ID del catálogo a eliminar
delete_query = {'id': catalog_id}
catalogs_collection.delete_one(delete_query)
