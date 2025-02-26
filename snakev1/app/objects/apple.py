from app.snake.interfaces.position import Position
import random

class Apple(Position):

    def __init__(self, range_map, id):
        self.id = id
        super().__init__()
        self.__random_state(range_map)

    def __random_state(self, range_map):
        self.x = random.randint(1,range_map-2)
        self.y = random.randint(1,range_map-2)
        




