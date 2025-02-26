from app.snake.tail import Tail
import random

class SnakeBuilder:
    def __init__(self):
        self.last_tail: Tail = False

    def create_head(self, range_map):
        self.last_tail = Tail(random.randint(1,1),
                              random.randint(1,1))
        return self.last_tail

    def create_tail(self):
        self.last_tail.prev = Tail(0,0)
        self.last_tail.last = False





