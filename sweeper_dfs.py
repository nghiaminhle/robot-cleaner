from sweeper import Sweeper
from robot import Robot
from utils import print_progress_matrix
from position import Position
from queue import Queue
from math import fabs

class SweeperDFS(Sweeper):

    def find_path(self, maps, from_position: Position):
        adj_stack = []
        visited = dict()
        previous = dict()
        adj_stack.append(from_position)
        target_position = None

        while len(adj_stack)>0:
            position = adj_stack.pop()
            if not position.pos() in visited.keys():
                visited[position.pos()] = True
                if maps[position.y][position.x] == 0:
                    target_position = position
                    break
                pos = Position(position.x + 1, position.y)
                if position.x < len(maps[0]) - 1 and maps[position.y][position.x + 1] >= 0 and not pos.pos() in visited.keys():
                    adj_stack.append(pos)
                    previous[pos.pos()] = position
                pos = Position(position.x, position.y + 1)
                if position.y < len(maps) - 1 and maps[position.y + 1][position.x] >= 0 and not pos.pos() in visited.keys():
                    adj_stack.append(pos)
                    previous[pos.pos()] = position
                pos = Position(position.x - 1, position.y)
                if position.x > 0 and maps[position.y][position.x - 1] >= 0 and not pos.pos() in visited.keys():
                    adj_stack.append(pos)
                    previous[pos.pos()] = position
                pos = Position(position.x, position.y - 1)
                if position.y > 0 and maps[position.y - 1][position.x] >= 0 and not pos.pos() in visited.keys():
                    adj_stack.append(pos)
                    previous[pos.pos()] = position

        path = self.get_path(from_position, target_position, previous)
    
        return path, target_position