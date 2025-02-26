from abc import abstractmethod,ABC 
from position import Position

class Movement(ABC,Position): 
    @abstractmethod
    def __init__(self):
        """метод инициализации движения
            необходимы параметры скорости движения 
            по направлениям x и y"""
        pass

    @abstractmethod
    def move(self,x,y):
        """метод изменяющий значение положения"""