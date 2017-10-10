from robot import Robot
from utils import print_progress_matrix, print_matrix
from position import Position
from queue import Queue
from math import fabs


class Sweeper:
    robot = None
    observed_maps = None

    def __init__(self, robot: Robot, maps):
        self.robot = robot
        self.observed_maps = maps
        self.look_around()
        self.observed_maps[self.robot.position.y][self.robot.position.x] = 1

    def work(self):
        start_position = self.robot.position
        while True:
            path, uncleaned_position = self.find_path(self.observed_maps, start_position)
            if uncleaned_position == None:
                break
            self.move_robot(path)
            self.observed_maps[uncleaned_position.y][uncleaned_position.x] += 1
            self.look_around()
            start_position = uncleaned_position
            
            #print_progress_matrix(self.robot.maps)
            #print_matrix(self.observed_maps)
            #input('press any key...')

    def look_around(self):
        if self.robot.has_uncleaned_cell(direction=0) and self.observed_maps[self.robot.position.y][self.robot.position.x + 1] < 0:
            self.observed_maps[self.robot.position.y][self.robot.position.x + 1] = 0
        
        if self.robot.has_uncleaned_cell(direction=1) and self.observed_maps[self.robot.position.y + 1][self.robot.position.x] < 0:
            self.observed_maps[self.robot.position.y+1][self.robot.position.x] = 0
        
        if self.robot.has_uncleaned_cell(direction=2) and self.observed_maps[self.robot.position.y][self.robot.position.x - 1] < 0:
            self.observed_maps[self.robot.position.y][self.robot.position.x - 1] = 0
        
        if self.robot.has_uncleaned_cell(direction=3) and self.observed_maps[self.robot.position.y - 1][self.robot.position.x] < 0:
            self.observed_maps[self.robot.position.y -1][self.robot.position.x] = 0

    def move_robot(self, path):
        while len(path) > 0:
            next_pos = path.pop()
            #print('-->', next_pos.pos())
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
            elif fabs(rotate) == 2:
                # turn back
                self.robot.turn_left()
                self.robot.turn_left()
            self.robot.move()

    def find_path(self, maps, from_position: Position):
        return None, None

    def get_path(self, from_position, to_position, previous_log):
        path = []
        if to_position != None:
            pos = to_position.pos()
            path.append(to_position)
            while pos in previous_log.keys():
                previous_position = previous_log[pos]
                pos = previous_position.pos()
                if previous_position.x != from_position.x or previous_position.y != from_position.y:
                    path.append(previous_position)
        return path
