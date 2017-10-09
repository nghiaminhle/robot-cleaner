class Position:
    x = 0
    y = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def pos(self):
        return "{}-{}".format(self.x, self.y)