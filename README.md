# 🚀 Pol's Asteroids Game 🎮✨

Welcome to **Pol's Asteroids Game**, where classic arcade fun meets modern gaming magic! 🌟 Pilot your spaceship, dodge and blast those pesky asteroids, and aim for the high score in this thrilling Python and Pygame adventure.

![Screenshot 2024-12-02 at 10 03 43](https://github.com/user-attachments/assets/de6bd481-f417-4233-a273-775ae54a30cc)

<div align="center">
  <a href="https://pelusinnidev.craft.me/AsteroidsGame">Check out the Report and Developer Notes (Available in Catalan)</a>
</div>

## 🌌 Game Overview

Embark on an interstellar journey through an ever-challenging asteroid field! In **Pol's Asteroids**, you control a nimble spaceship with the mission to survive as long as possible by destroying asteroids and racking up points. With progressive difficulty and dynamic gameplay, every round promises a fresh and exciting experience.

## 🚀 Features

- **✨ Smooth Vector Graphics**: Crisp visuals at any resolution, ensuring your spaceship and asteroids look sharp and stylish!
- **🛠 Physics-Based Movement**: Experience realistic momentum and ship controls that make flying an immersive experience.
- **📈 Progressive Difficulty**: Each round ramps up the challenge with more asteroids and faster speeds. Can you keep up?
- **🔢 Round System**: Track your progression with the current round displayed prominently on the screen.
- **🎵 Dynamic Sound System**:
  - 🎶 **Menu Music**: Groove to the beats while navigating the main menu.
  - 🎮 **Game Music**: Intense tracks that keep you pumped during gameplay.
  - 💀 **Game Over Effects**: Hear the sounds of defeat when things get tough.
- **🕹 Multiple Game States**:
  - 🏠 **Main Menu**
  - 🎮 **Gameplay**
  - ⏸ **Pause Menu**
  - 🛑 **Game Over Screen**
  - 🏆 **High Scores Entry**
  
## 🎮 Controls

Take command of your spaceship with ease! Whether you prefer arrow keys or WASD, mastering the controls is a breeze:

- **🚀 Movement**:
  - **↑ / W**: Thrust forward
  - **↓ / S**: Thrust backward
  - **← / A**: Rotate ship left
  - **→ / D**: Rotate ship right
- **💥 Actions**:
  - **SPACE**: Fire projectiles
  - **ESC**: Pause game
  - **F11**: Toggle fullscreen

## 🎨 Visual Elements

- **🚀 Spaceship**: Sleek vector-based design with a cool thrust animation.
- **🪨 Asteroids**: Procedurally generated with three distinct sizes:
  - **Large**: 40 radius
  - **Medium**: 20 radius
  - **Small**: 10 radius
- **💫 Projectiles**: Light-based shooting effects that leave a trail.
- **🖥 UI Elements**: Clean, arcade-style interface that keeps you informed without clutter.
- **📽 Intro Slides**: Flashing developer and partner logos with smooth fade transitions.

## 🏆 Scoring System

Rack up points by destroying asteroids! Here's how it breaks down:

- **Large Asteroid**: 🥉 20 points
- **Medium Asteroid**: 🥈 50 points
- **Small Asteroid**: 🥇 100 points

## 🔄 Round System

Survive and thrive through multiple rounds, each more challenging than the last!

- **Round Display**: Current round shown on the top-right corner.
- **Asteroid Count**: Increases by 1 each round.
- **Asteroid Speed**: Accelerates by 10% each round, capped at 2x the base speed.
  
**Example Progression**:
- **Round 1**: 3 asteroids at normal speed.
- **Round 5**: 7 asteroids at 1.4x speed.
- **Round 10**: 12 asteroids at 2x speed.
- **Round 15+**: Asteroid count continues to rise while speed remains capped.

## 🛠 Setup and Installation

Get ready to blast off! Follow these simple steps to set up the game on your machine:

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/pelusinnidev/Pols-Asteroids.git
    cd Pols-Asteroids
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

## 🎉 Contributing

We love contributions! Whether it's a bug fix, a new feature, or just some awesome ideas, feel free to open an issue or submit a pull request. Let's make **Pol's Asteroids** even more awesome together! 🤝

---

![Developer](https://github.com/pelusinnidev/Pols-Asteroids/blob/main/src/assets/images/developer_logo.jpg?raw=true)  
**A Game By PelusinniDev**  
![La Salle Gràcia](https://github.com/pelusinnidev/Pols-Asteroids/blob/main/src/assets/images/lasalle_logo.jpg?raw=true)  
**La Salle Gràcia**

Check out the project on [GitHub](https://github.com/pelusinnidev/Pols-Asteroids) for more details and updates!
