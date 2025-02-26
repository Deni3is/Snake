from app.snake.interfaces.position import Position
from app.snake.snake import Snake
from app.objects.apple import Apple
import os, time, copy
from app.controller.controller import Controller
import threading

class Map:
    def __init__(self, size_map):
        self.all_object: list[Apple] = []
        self.snake = Snake(size_map)

        self.controoler =Controller(self.snake)
        
        self.controoler = threading.Thread(target = self.controoler.move)
        self.controoler.start()

        self.size_map = size_map
        apple = Apple(size_map, 0)
        self.all_object.append(apple) 
        self.end = False
        self.game_speed = 0.5
        self.main_thread = threading.Thread(target = self.visualise_map, args=(size_map,))
        self.main_thread.start()


    def __del__(self):  
        self.main_thread.join()

    
    def visualise_map(self,size_map):
        map_coordinate = [['  ' for _ in range(size_map)] for _ in range(size_map)]
        map_coordinate[0][0] = "--"
        map_coordinate[size_map-1][0] = "--"
        for i in range(1,size_map-1):
            map_coordinate[i][0] = "|"
            map_coordinate[i][size_map-1] = "|"
            map_coordinate[0][i] = "--"
            map_coordinate[size_map-1][i] = "--"
        
        copy_map =  copy.deepcopy(map_coordinate)

        self.snake.start_move(1,0)
        try:
            while not self.end:
                os.system('cls' if os.name == 'nt' else 'clear')
                copy_map = copy.deepcopy(map_coordinate)
                self.change_position_object(copy_map)
                self.create_static_object(copy_map)
                for i in range(size_map):
                    print("".join(copy_map[i]))
                time.sleep(self.game_speed)

        except KeyboardInterrupt:
            print("\nВыход из программы.")


    def change_position_object(self, map_coordinate):
        self.snake.move_snake()
        for object in self.all_object:
            self.collision(object, self.snake)
        self.snake_collision(self.snake)
        snake_position_list = self.snake.get_position()
        if isinstance(snake_position_list[0],tuple):
            for position in snake_position_list:
                if position is not None:
                    if position[0]>=0 and position[0]<self.size_map and position[1]>=0 and position[1]<self.size_map: 
                        map_coordinate[position[0]][position[1]] = "*"
                    else:
                        self.game_over()
        else:
            if snake_position_list[0]>=0 and snake_position_list[0]<self.size_map and \
            snake_position_list[1]>=0 and snake_position_list[1]<self.size_map: 
                map_coordinate[snake_position_list[0]][snake_position_list[1]] = "*"
            else:
                self.game_over()

    def create_static_object(self, map_coordinate):
        for object in self.all_object:
            xy = object.get_position()
            map_coordinate[xy[0]][xy[1]] = "🍎"

        

    def collision(self,object1: Position, object2: Snake):
        list_objects_coord = object1.get_position(),object2.get_position()
        if len(list_objects_coord) != len(set(list_objects_coord)):
            self.snake.eat_apple()
            last_id = object1.id
            self.all_object.remove(object1)
            self.all_object.append(Apple(self.size_map,last_id))


    def snake_collision(self, object: Snake):
        snake = object.get_position()
        if len(snake) != len(set(snake)):
            print("Коллизия змеи")
            self.game_over()


    def game_over(self):
        self.end = True
        print("GAME OVER")



    

        
