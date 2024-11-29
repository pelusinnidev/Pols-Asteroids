# Pol's Asteroids Game

A modern take on the classic Asteroids arcade game, built with Python and Pygame.

## 🎮 Game Overview

In Pol's Asteroids, you pilot a spaceship through an asteroid field. Your mission is to survive while destroying asteroids and achieving the highest score possible. The game features a robust round system that increases the challenge progressively, ensuring an engaging and dynamic gameplay experience.

## 🚀 Features

- **Smooth Vector Graphics**: All game elements are rendered using vector graphics for crisp visuals at any resolution.
- **Physics-Based Movement**: Realistic momentum-based ship controls.
- **Progressive Difficulty**: Each round increases the challenge with more asteroids and higher asteroid speeds.
- **Round System**: Displays the current round on the screen, tracking your progression.
- **Dynamic Sound System**: Immersive audio experience with:
  - Menu music
  - Game music
  - Game over effects
- **Multiple Game States**:
  - Main Menu
  - Gameplay
  - Pause Menu
  - Game Over Screen
  - High Scores Entry

## 🎯 Controls

- **Movement**:
  - Arrow Keys or WASD for ship control
  - ↑/W: Thrust forward
  - ↓/S: Thrust backward
  - ←/A, →/D: Rotate ship
- **Actions**:
  - SPACE: Fire projectiles
  - ESC: Pause game
  - F11: Toggle fullscreen

## 🎵 Audio System

The game features a dynamic audio system that changes based on game state:
1. **Menu Music**: Plays in a loop while in the main menu.
2. **Game Music**: Transitions to game music during gameplay.
3. **Game Over Sound**: Plays a sound effect when the player dies.
4. **Return to Menu Music**: After game over, music transitions back to the menu theme.

## 🎨 Visual Elements

- **Spaceship**: Vector-based design with thrust animation.
- **Asteroids**: Procedurally generated shapes in three sizes:
  - Large (40 radius)
  - Medium (20 radius)
  - Small (10 radius)
- **Projectiles**: Light-based shooting effects.
- **UI Elements**: Clean, arcade-style interface.
- **Intro Slides**: Displays developer and partner logos with fade-in and fade-out transitions.

## 💯 Scoring System

- **Large Asteroid**: 20 points
- **Medium Asteroid**: 50 points
- **Small Asteroid**: 100 points

## 🔁 Round System

- **Round Display**: The current round is displayed on the top-right corner of the screen.
- **Progressive Difficulty**:
  - **Asteroid Count**: Increases by 1 each round (e.g., 3 asteroids in Round 1, 4 in Round 2, etc.).
  - **Asteroid Speed**: Increases by 10% each round, capped at 2x the base speed to ensure the game remains challenging yet fair.
  - **Example Progression**:
    - Round 1: 3 asteroids at normal speed.
    - Round 5: 7 asteroids at 1.4x speed.
    - Round 10: 12 asteroids at 2x speed.
    - Round 15+: Asteroid count continues to increase while speed remains capped.

## 🔧 Technical Details

- **Screen Resolution**: 1280x720 (default).
- **Framerate**: 60 FPS.
- **Configurable Fullscreen Support**: Toggle fullscreen mode using F11.
- **Physics Parameters**:
  - Ship acceleration: 0.15
  - Maximum speed: 4
  - Rotation speed: 5
  - Friction: 0.98
- **Asteroid Configuration**:
  - **Speeds**:
    - Large: 1
    - Medium: 2
    - Small: 3
  - **Scores**:
    - Large: 20
    - Medium: 50
    - Small: 100
- **High Score Management**:
  - Saves top 8 high scores.
  - Allows players to enter their name upon achieving a high score.
  - High scores are persisted in a JSON file.

## 📂 Project Structure

```
src/
├── assets/
│   ├── fonts/
│   │   ├── PressStart2P-Regular.ttf
│   │   └── OFL.txt
│   ├── images/
│   │   ├── developer_logo.jpg
│   │   ├── lasalle_logo.jpg
│   │   └── placeholder.jpg
│   └── music/
│       ├── menu_music.mp3
│       ├── game_music.mp3
│       └── game_over.mp3
├── core/
│   ├── engine/
│   │   ├── collision_system.py
│   │   └── game_engine.py
│   └── managers/
│       ├── sound_manager.py
│       └── high_score_manager.py
├── entities/
│   ├── base_entity.py
│   ├── enemies/
│   │   ├── __init__.py
│   │   ├── enemy_behaviors.py
│   │   └── enemy_ship.py
│   ├── objects/
│   │   ├── asteroid.py
│   │   ├── powerup.py
│   │   └── projectile.py
│   └── player/
│       ├── __init__.py
│       ├── spaceship.py
│       └── weapons.py
├── scenes/
│   ├── __init__.py
│   ├── game_scene.py
│   ├── intro_scene.py
│   ├── menu_scene.py
│   └── pause_scene.py
├── ui/
│   ├── components/
│   │   ├── button.py
│   │   ├── health_bar.py
│   │   └── menu.py
│   └── hud.py
└── utils/
    ├── constants.py
    └── transitions.py
.idea/
├── modules.xml
├── misc.xml
└── pr-pygame-24-25-pelusinnidev.iml
main.py
README.md
```

## 🛠 Setup and Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/pols-asteroids.git
    cd pols-asteroids
    ```

2. **Create a Virtual Environment**:
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Game**:
    ```bash
    python src/main.py
    ```

## 📝 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 👥 Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## 📫 Contact

For any inquiries or feedback, please contact [your.email@example.com](mailto:your.email@example.com).
