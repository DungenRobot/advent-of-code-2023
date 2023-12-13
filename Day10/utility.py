from __future__ import annotations

class vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other: vector) -> bool:
        return (self.x == other.x) and (self.y == other.y)
    def __ne__(self, other: vector) -> bool:
        return not (self == other)
    
    def __add__(self, other:vector) -> vector:
        return vector(self.x + other.x, self.y + other.y)
    def __sub__(self, other: vector) -> vector:
        return vector(self.x - other.x, self.y - other.y)
    
    def __neg__(self) -> vector:
        return vector(-self.x, -self.y)


    def set_from_string(self, info: str):
        info.strip('()')
        x, y = info.split(", ")
        self.x, self.y = int(x), int(y)
    def __repr__(self) -> str:
        return "(%s, %s)" % (self.x, self.y)

UP = vector(0, 1)
DOWN = vector(0, -1)
LEFT = vector(-1, 0)
RIGHT = vector(1, 0)

array_directions = [UP, DOWN, LEFT, RIGHT]
