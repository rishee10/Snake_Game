# Snake Game using FastAPI & Vanilla JavaScript

This project implements a classic Snake game where the snake moves automatically and changes direction when arrow keys are pressed. The backend game logic, including snake movement, food placement, and collision detection, is handled by FastAPI, and the UI is created using HTML, CSS & JavaScript.

## Features

Snake moves continuously and grows when it eats food

Fully controlled by arrow keys

Score tracking

Game Over detection

Grid-based visual board

## How to Run the Game

#### Clone this repository:

```
git clone https://github.com/rishee10/Snake_Game.git
```

```
cd Snake_Game
```

#### Create Virtual Enviroment and activate it

```
python -m venv venv
```

```
venv/Scripts/activate
```


#### Download the Requirements

```
pip install fastapi uvicorn
```

#### Run the Server

```
uvicorn main:app --reload
```

