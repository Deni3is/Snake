from app.snake.state import Speed
from app.snake.snakebuilder import SnakeBuilder
from app.snake.tail import Tail

class Snake(Speed):

    def __init__(self, range_map):
        Speed.__init__(self)
        self.creator_tail = SnakeBuilder()
        self.snake_head: Tail = self.creator_tail.create_head(range_map)

    def extension(self):
        self.creator_tail.create_tail()

    def move_snake(self):
        self.snake_head.move(self.duration_x,self.duration_y)

    def eat_apple(self):
        self.extension()

    def start_move(self, x, y):
        # print("Змея начала ползти", x, y)     
        self.duration_x = x
        self.duration_y = y

    def position(self):
        return self.snake_head.x, self.snake_head.y
    
    def get_position(self):
        return self.snake_head.get_position_recursive()