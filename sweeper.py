from robot import Robot
from utils import print_progress_matrix
from position import Position
from queue import Queue
from math import fabs

class Sweeper:
    robot = None
    maps = None

    def __init__(self, robot: Robot, maps):
        self.robot = robot
        self.maps = maps
    
    def work(self):
        start_position = self.robot.position
        while True:
            path, uncleaned_position = self.find_path(self.maps, start_position)
            if uncleaned_position == None:
                break
            self.move_robot(path)
            start_position = uncleaned_position
            #print_progress_matrix(self.maps)
    
    def move_robot(self, path):
         while len(path)>0:
            next_pos = path.pop()
            direction = 0
            if next_pos.x == self.robot.position.x + 1:
                direction = 0
            if next_pos.y == self.robot.position.y + 1:
                direction = 1
            if next_pos.x == self.robot.position.x - 1:
                direction = 2
            if next_pos.y == self.robot.position.y - 1:
                direction = 3
            rotate = direction - self.robot.direction
            if rotate == -1 or rotate == 3:
                self.robot.turn_left()
            elif rotate == 1 or rotate == -3:
                self.robot.turn_right()
            elif fabs(rotate)==2:
                # turn back
                self.robot.turn_left()
                self.robot.turn_left()
            self.robot.move()

    def find_path(self, maps, from_position: Position):
        return None, None