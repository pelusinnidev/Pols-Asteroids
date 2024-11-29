from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os
import certifi

load_dotenv()

MONGO_URI = os.getenv('MONGO_URI')
DB_NAME = os.getenv('DB_NAME')

print(f"Intentando conectar a MongoDB con URI: {MONGO_URI}")
print(f"Base de datos objetivo: {DB_NAME}")

def get_database():
    try:
        client = MongoClient(
            MONGO_URI,
            server_api=ServerApi('1'),
            tlsCAFile=certifi.where(),
            serverSelectionTimeoutMS=5000,
            connectTimeoutMS=5000,
            socketTimeoutMS=5000
        )
        
        print("Intentando hacer ping a MongoDB...")
        client.admin.command('ping')
        print("¡Conexión exitosa a MongoDB!")
        
        print(f"Intentando acceder a la base de datos: {DB_NAME}")
        db = client[DB_NAME]
        return db
    except Exception as e:
        print(f"Error detallado de conexión a MongoDB: {str(e)}")
        print(f"Tipo de error: {type(e)}")
        print(f"Certificado SSL usado: {certifi.where()}")
        return None 