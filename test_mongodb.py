from src.core.managers.mongo_high_score_manager import MongoHighScoreManager

# Crear instancia del gestor
score_manager = MongoHighScoreManager()

# Añadir algunas puntuaciones de prueba
print('\nAñadiendo puntuaciones de prueba...')
test_scores = [
    ('AAA', 1000),
    ('BBB', 800),
    ('CCC', 600)
]

for name, score in test_scores:
    success = score_manager.add_high_score(name, score)
    print(f'Añadiendo {name}: {score} - {"Éxito" if success else "Error"}')

# Obtener y mostrar todas las puntuaciones
print('\nPuntuaciones guardadas:')
high_scores = score_manager.get_high_scores()
for score in high_scores:
    print(f'Nombre: {score["name"]}, Puntuación: {score["score"]}')

# Mostrar mensaje de estado
print(f'\nEstado: {score_manager.get_status_message()}') 