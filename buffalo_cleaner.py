from random import randint


class Robot:
    maps = None
    x = 0
    y = 0
    square = 0
    direction = 0
    rows = 0
    cols = 0
    cleaned_number = 0

    def __init__(self, maps, square, x, y, direction):
        self.maps = maps
        self.x = x
        self.y = y
        self.square = square
        self.direction = direction
        self.rows = len(self.maps)
        self.cols = len(self.maps[0])

    def run(self):
        while True:
            candidate = self.direct()
            if self.can_move(candidate):
                self.direction = candidate  
                self.move()
            if self.cleaned_number == self.square:
                break
        print(self.maps)

    def direct(self):
        directions = []
        leff = self.turn_left(self.direction)
        if (self.can_move(leff)):
            directions.append(leff)
        right = self.turn_right(self.direction)
        if (self.can_move(right)):
            directions.append(right)

        l = len(directions)
        if (l > 0):
            return directions[randint(0, l-1)]
        else:
            return self.turn_left(self.turn_left(self.direction))

    def turn_left(self, direction):
        if (direction - 1 >= 0):
            return direction - 1
        return 3

    def turn_right(self, direction):
        return int((direction + 1) % 4)

    def can_move(self, direction):
        if direction == 0 and self.x < self.cols - 1 and self.maps[self.x + 1][self.y] >= 0:
            return True
        if direction == 1 and self.y < self.rows - 1 and self.maps[self.x][self.y + 1] >= 0:
            return True
        if direction == 2 and self.x >0 and self.maps[self.x-1][self.y] >= 0:
            return True
        if direction == 3 and self.y > 0 and self.maps[self.x][self.y - 1] >= 0:
            return True
        return False

    def move(self):
        if self.direction == 0:
            self.x += 1
        if self.direction == 1:
            self.y += 1
        if self.direction == 2:
            self.x -= 1
        if self.direction == 3:
            self.y -= 1
        print(self.cleaned_number, self.direction, self.x, self.y, self.maps)
        if (self.maps[self.x][self.y] == 0):
            self.cleaned_number += 1
            self.maps[self.x][self.y] = 1
        else:
            self.maps[self.x][self.y] += 1

def main():
    maps = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, -1, -1],
    ]
    robot = Robot(maps, 14, 0, 1, 1)
    robot.run()

if __name__ == "__main__":
    main()
