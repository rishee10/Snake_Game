from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import random

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Game state
snake = [{"x": 8, "y": 8}]
direction = "RIGHT"
food = {"x": random.randint(0, 19), "y": random.randint(0, 19)}
score = 0
board_size = 20

class Move(BaseModel):
    direction: str  # LEFT, RIGHT, UP, DOWN

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("snake.html", {"request": request})

@app.post("/move")
def move_snake(move: Move):
    global snake, direction, food, score
    new_dir = move.direction.upper()
    
    # reverse direction
    if (new_dir == "LEFT" and direction != "RIGHT") or \
       (new_dir == "RIGHT" and direction != "LEFT") or \
       (new_dir == "UP" and direction != "DOWN") or \
       (new_dir == "DOWN" and direction != "UP"):
        direction = new_dir

    head = snake[0].copy()
    if direction == "LEFT":
        head["x"] -= 1
    elif direction == "RIGHT":
        head["x"] += 1
    elif direction == "UP":
        head["y"] -= 1
    elif direction == "DOWN":
        head["y"] += 1

    # collisions
    if head["x"] < 0 or head["x"] >= board_size or head["y"] < 0 or head["y"] >= board_size \
       or head in snake:
        snake = [{"x": 8, "y": 8}]
        direction = "RIGHT"
        food = {"x": random.randint(0, 19), "y": random.randint(0, 19)}
        score = 0
        return JSONResponse({"game_over": True, "score": score})

    # Move snake
    snake.insert(0, head)

    # Check if food eaten by the snake
    if head == food:
        score += 1
        food = {"x": random.randint(0, 19), "y": random.randint(0, 19)}
    else:
        snake.pop()  # remove tail if no food eaten by snake

    return {
        "snake": snake,
        "food": food,
        "score": score,
        "game_over": False
    }
