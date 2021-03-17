import math


class Position:
    """(x,y)"""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move_position(self, position):
        self.x += position.x
        self.y += position.y

    def distance_to(self, other_position):
        return math.sqrt(((self.x - other_position.x) ** 2) + ((self.y - other_position.y) ** 2))

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        return (self.x < other.x) and (self.y < other.y)

    def __hash__(self):
        return hash(hash(self.x) + hash(self.y))
