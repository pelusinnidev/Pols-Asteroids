import os
import json
import platform

class HighScoreManager:
    def __init__(self, max_scores=8):
        # Determina el directori de configuració de l'usuari segons el sistema operatiu
        if platform.system() == "Windows":
            config_dir = os.path.join(os.environ['APPDATA'], "PolsAsteroids")
        elif platform.system() == "Darwin":
            config_dir = os.path.expanduser("~/Library/Application Support/PolsAsteroids")
        else:
            config_dir = os.path.expanduser("~/.pols_asteroids")
        
        os.makedirs(config_dir, exist_ok=True)
        self.file_path = os.path.join(config_dir, "high_scores.json")
        self.max_scores = max_scores
        self.high_scores = []
        self.load_high_scores()

    def load_high_scores(self):
        """Carrega les puntuacions des del fitxer JSON."""
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, "r") as file:
                    self.high_scores = json.load(file)
                print("High scores carregades correctament.")
            except (json.JSONDecodeError, IOError) as e:
                print(f"Error carregant high scores: {e}")
                self.high_scores = []
                self.save_high_scores()
        else:
            self.high_scores = []
            self.save_high_scores()
            print("No s'ha trobat el fitxer de high scores. Creat un nou fitxer buit.")

    def save_high_scores(self):
        """Guarda les puntuacions al fitxer JSON."""
        try:
            with open(self.file_path, "w") as file:
                json.dump(self.high_scores, file, indent=4)
            print("High scores guardades correctament.")
        except IOError as e:
            print(f"Error guardant high scores: {e}")

    def is_high_score(self, score):
        """Verifica si una puntuació és suficient per entrar a les high scores."""
        if len(self.high_scores) < self.max_scores:
            return True
        return score > self.high_scores[-1]['score']

    def add_high_score(self, name, score):
        """Afegeix una nova puntuació i manté la llista ordenada."""
        self.high_scores.append({'name': name, 'score': score})
        self.high_scores = sorted(self.high_scores, key=lambda x: x['score'], reverse=True)[:self.max_scores]
        self.save_high_scores()
        print(f"Puntuació alta afegida: {name} - {score}")

    def get_high_scores(self):
        """Retorna la llista de high scores."""
        return self.high_scores
