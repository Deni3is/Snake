import keyboard 
from app.snake.snake import Snake
import threading
import time

class Controller:
    def __init__(self, snake:Snake):
        self.snake = snake
        self.lock = threading.Lock()

    def move(self):
        while True:
            try:  
                if keyboard.is_pressed('w'):  
                    with self.lock:
                        self.snake.start_move(-1,0)
                elif keyboard.is_pressed('a'):
                    with self.lock:
                        self.snake.start_move(0,-1)
                elif keyboard.is_pressed('s'):
                    with self.lock:
                        self.snake.start_move(1,0)
                elif keyboard.is_pressed('d'):
                    with self.lock:
                        self.snake.start_move(0,1)
            except:
                print("Error controller")
            time.sleep(0.1)