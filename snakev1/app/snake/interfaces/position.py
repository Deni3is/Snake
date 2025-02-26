
from abc import abstractmethod,ABC 
    
class Position(ABC): 
    @abstractmethod
    def __init__(self):
        self.x = 0
        self.y = 0

    def get_position(self):
        return (self.x, self.y)



