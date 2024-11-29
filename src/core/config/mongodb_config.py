from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os
import urllib.parse
import certifi

load_dotenv()

# Obtener el URI de MongoDB y el nombre de la base de datos desde las variables de entorno
raw_uri = os.getenv('MONGODB_URI')
DB_NAME = os.getenv('MONGODB_DB_NAME')
COLLECTION_NAME = 'Scores'

# Parsear y reconstruir el URI con componentes codificados si es necesario
if raw_uri and '@' in raw_uri:
    try:
        # Dividir el URI en partes
        prefix = raw_uri.split('://', 1)[0]
        rest = raw_uri.split('://', 1)[1]
        credentials = rest.split('@')[0]
        host = rest.split('@', 1)[1]
        
        # Dividir las credenciales
        username = credentials.split(':', 1)[0]
        password = credentials.split(':', 1)[1]
        
        # Codificar el nombre de usuario y la contraseña
        encoded_username = urllib.parse.quote_plus(username)
        encoded_password = urllib.parse.quote_plus(password)
        
        # Reconstruir el URI
        MONGO_URI = f"{prefix}://{encoded_username}:{encoded_password}@{host}"
    except Exception as e:
        print(f"Error al procesar el URI de MongoDB: {e}")
        MONGO_URI = raw_uri
else:
    MONGO_URI = raw_uri

print(f"Base de datos: {DB_NAME}")
print(f"Colección: {COLLECTION_NAME}")

def get_database():
    try:
        # Crear un nuevo cliente y conectarse al servidor
        client = MongoClient(
            MONGO_URI,
            server_api=ServerApi('1'),
            tlsCAFile=certifi.where()  # Añadir certificado SSL
        )
        
        # Enviar un ping para confirmar una conexión exitosa
        try:
            client.admin.command('ping')
            print("¡Conexión exitosa a MongoDB!")
            
            # Obtener la base de datos y la colección
            db = client[DB_NAME]
            collection = db[COLLECTION_NAME]
            # Probar el acceso a la colección
            collection.find_one()
            print(f"¡Acceso exitoso a la base de datos {DB_NAME} y colección {COLLECTION_NAME}!")
            return db
        
        except Exception as e:
            print(f"Error de conexión: {e}")
            return None
        
    except Exception as e:
        print(f"Error al crear el cliente: {e}")
        return None 