from pymongo import MongoClient, DESCENDING, ASCENDING
from src.core.config.mongodb_config import get_database, COLLECTION_NAME

class MongoHighScoreManager:
    def __init__(self, max_scores=8):
        self.db = get_database()
        self.max_scores = max_scores
        self.high_scores = []
        self.status_message = ""
        self.collection = None
        
        if self.db is not None:
            try:
                self.collection = self.db[COLLECTION_NAME]
                # Crear índice en el campo 'score' descendente
                try:
                    self.collection.create_index([("score", DESCENDING)])
                except Exception as e:
                    print(f"No se pudo crear el índice, pero continuamos: {e}")
                self.load_high_scores()
            except Exception as e:
                print(f"Error al inicializar la colección: {e}")
                self.status_message = "Error al inicializar la conexión con MongoDB"
        else:
            self.status_message = "No se pudo conectar a MongoDB"
        
    def load_high_scores(self):
        """Carga las puntuaciones desde MongoDB."""
        if self.collection is None:
            self.status_message = "No hay conexión con MongoDB"
            return
            
        self.status_message = "Cargando puntuaciones..."
        try:
            # Cargar ordenado por posición
            self.high_scores = list(
                self.collection.find({}, {'_id': 0})
                .sort('score', DESCENDING)
                .limit(self.max_scores)
            )
            self.status_message = "Puntuaciones cargadas correctamente"
            print("High scores cargadas correctamente desde MongoDB.")
        except Exception as e:
            self.status_message = f"Error al cargar puntuaciones: {str(e)}"
            print(f"Error cargando high scores desde MongoDB: {e}")
            self.high_scores = []
            
    def save_high_scores(self):
        """Guarda las puntuaciones en MongoDB."""
        if self.collection is None:
            self.status_message = "No hay conexión con MongoDB"
            return
            
        self.status_message = "Guardando puntuaciones..."
        try:
            # Actualizar usando upsert
            for i, score in enumerate(self.high_scores):
                self.collection.update_one(
                    {"position": i},
                    {
                        "$set": {
                            "name": score["name"],
                            "score": score["score"],
                            "position": i
                        }
                    },
                    upsert=True
                )
            
            # Eliminar puntuaciones antiguas que ya no están en el top
            self.collection.delete_many({"position": {"$gte": len(self.high_scores)}})
            
            self.status_message = "Puntuaciones guardadas correctamente"
            print("High scores guardadas correctamente en MongoDB.")
        except Exception as e:
            self.status_message = f"Error al guardar puntuaciones: {str(e)}"
            print(f"Error guardando high scores en MongoDB: {e}")
            
    def is_high_score(self, score):
        """Verifica si una puntuación es suficiente para entrar en las high scores."""
        if len(self.high_scores) < self.max_scores:
            return True
        return score > self.high_scores[-1]['score'] if self.high_scores else True

    def add_high_score(self, name, score):
        """Añade una nueva puntuación y mantiene la lista ordenada."""
        if not isinstance(name, str) or not isinstance(score, (int, float)):
            self.status_message = "Error: formato de datos inválido"
            return False
            
        if len(name) > 3:  # Limitar nombres a 3 caracteres en el juego
            name = name[:3]
            
        self.status_message = "Añadiendo nueva puntuación..."
        new_score = {'name': name, 'score': score}
        self.high_scores.append(new_score)
        self.high_scores = sorted(
            self.high_scores, 
            key=lambda x: x['score'], 
            reverse=True
        )[:self.max_scores]
        
        # Intentar guardar en MongoDB si hay conexión
        if self.collection is not None:
            self.save_high_scores()
            return True
        else:
            self.status_message = "Puntuación guardada localmente (sin conexión a MongoDB)"
            return False

    def get_high_scores(self):
        """Retorna la lista de high scores."""
        if len(self.high_scores) == 0 and self.collection is not None:
            self.load_high_scores()
        return self.high_scores

    def get_status_message(self):
        """Retorna el mensaje de estado actual."""
        return self.status_message

    def clear_high_scores(self):
        """Elimina todas las puntuaciones."""
        if self.collection is not None:
            try:
                self.collection.delete_many({})
                self.high_scores = []
                self.status_message = "Puntuaciones eliminadas correctamente"
                return True
            except Exception as e:
                self.status_message = f"Error al eliminar puntuaciones: {str(e)}"
                return False
        else:
            self.status_message = "No hay conexión con MongoDB"
            return False