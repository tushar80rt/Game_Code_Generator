# GameForge AI - Game Code Generator

Transform your game ideas into reality—instantly!

## 🚀 Overview
**GameForge AI** is a Python-powered tool that uses AI agents to generate and run playable game code based on your description. Just describe your dream game, and the system will write, save, and launch a fully interactive Python game for you—no setup required!

## 🧩 Features
- **AI-Powered Game Generation:** Converts any game idea into runnable Python code.
- **Instant Play:** Games are generated and launched automatically.
- **No External Assets:** All games use built-in Python libraries—no need for images or sounds.
- **Multiple Game Types:** Supports arcade, grid-based, and advanced 2D games.
- **User Interaction:** Games always include playable logic and controls (keyboard/mouse).

## 🛠️ How It Works
1. **Describe** your dream game in the app.
2. **AI generates** Python code for your game.
3. **Game runs automatically**—ready to play!

## 💡 Usage Example

1. Launch the app:
   ```bash
   streamlit run app.py
   ```

2. Enter your game idea, e.g.:
   ```
   "A space shooter with power-ups and boss battles"
   ```

3. Click **Generate & Run Game**—your game will be created and launched!

## 📦 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/tushar80rt/Game_Code_Generator.git
   cd Game_Code_Generator
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Add your OpenAI API key to `api.env`.

## 🗂️ Project Structure

```
app.py                   # Streamlit web interface
agents/
  ├─ code_writer.py      # AI agent for code generation
  └─ code_runner.py      # AI agent for running code
api.env                  # Environment variables (API keys)
requirements.txt         # Python dependencies
```

## 🎮 Supported Game Types

- **Arcade:** Snake, Pong, Breakout (uses `turtle`)
- **Board/Grid:** Chess, Tic-Tac-Toe, Checkers (uses `tkinter`)
- **2D Action:** Platformers, Shooters (uses `pygame` with basic shapes/colors)

## 📞 Support

For issues or feedback, email: **tushar80rt@gmail.com**

© 2025 GameForge AI | Built with CAMEL-AI & OpenAI
