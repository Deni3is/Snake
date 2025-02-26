from app.snake.interfaces.position import Position

class Tail(Position):

    def __init__(self, x, y):
        super().__init__()
        self.prev: Tail = False
        self.last = True
        self.change_position(x, y)

    def move(self, x:int, y:int):
        """Если есть еще элементы, то они берут позицию до движения"""
        if not self.last:
            self.prev.change_position(self.x, self.y)
        #движение
        self.x += x
        self.y += y

    def change_position(self, x: int, y: int):
        if not self.last:
            self.prev.change_position(self.x, self.y)
        self.x = x
        self.y = y

    def get_position_recursive(self):
        if not self.last:
            return self.get_position(),self.prev.get_position_recursive()
        return self.get_position()
        
