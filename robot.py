class Robot:
    maps = None
    position = None
    direction = 0
    turn_number = 0
    step_number = 0
    paths = []

    def __init__(self, maps, position, direction):
        self.maps = maps
        self.position = position
        self.direction = direction
        self.maps[position.y][position.x] += 1
        self.log(self.position)

    def turn_left(self):
        self.direction = int((self.direction + 3) % 4)
        self.turn_number += 1

    def turn_right(self):
        self.direction = int((self.direction + 1) % 4)
        self.turn_number += 1

    def move(self):
        '''
            direction:
            0: move right
            1: move down
            2: move left
            3: move up
        '''
        if self.direction == 0 and self.position.x < len(self.maps[0]) - 1 and self.maps[self.position.y][self.position.x + 1] >= 0:
            self.position.x += 1
            self.maps[self.position.y][self.position.x] += 1
            self.step_number +=1
            self.log(self.position)
            return True
        if self.direction == 1 and self.position.y < len(self.maps) - 1 and self.maps[self.position.y + 1][self.position.x] >= 0:
            self.position.y += 1
            self.maps[self.position.y][self.position.x] += 1
            self.step_number +=1
            self.log(self.position)
            return True
        if self.direction == 2 and self.position.x > 0 and self.maps[self.position.y][self.position.x - 1] >= 0:
            self.position.x -= 1
            self.maps[self.position.y][self.position.x] += 1
            self.step_number +=1
            self.log(self.position)
            return True
        if self.direction == 3 and self.position.y > 0 and self.maps[self.position.y - 1][self.position.x] >= 0:
            self.position.y -= 1
            self.maps[self.position.y][self.position.x] += 1
            self.step_number +=1
            self.log(self.position)
            return True
        return False
    
    def log(self, position):
        self.paths.append(position)
