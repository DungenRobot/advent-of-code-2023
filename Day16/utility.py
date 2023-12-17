from __future__ import annotations

class vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other: vector) -> bool:
        return (self.x == other.x) and (self.y == other.y)
    def __ne__(self, other: vector) -> bool:
        return not (self == other)
    
    def __iadd__(self, other: vector):
        self.x += other.x
        self.y += other.y
    
    def __add__(self, other:vector) -> vector:
        return vector(self.x + other.x, self.y + other.y)
    def __sub__(self, other: vector) -> vector:
        return vector(self.x - other.x, self.y - other.y)
    
    def __neg__(self) -> vector:
        return vector(-self.x, -self.y)

    def get_tuple(self):
        return (self.x, self.y)

    def set_from_string(self, info: str):
        info.strip('()')
        x, y = info.split(", ")
        self.x, self.y = int(x), int(y)
    def __repr__(self) -> str:
        return "(%s, %s)" % (self.x, self.y)
    
    def is_within_bounds(self, x_min, x_max, y_min, y_max):
        return (x_min <= self.x < x_max) and (y_min <= self.y < x_max)

    def is_in_list(self, l: list[vector]):
        for other in l:
            if self == other:
                return True
        return False


class direction(vector):
    def __init__(self, dir: str):
        self.name = dir
        i: tuple[int, int]
        match dir:
            case "UP": i = (0, -1)
            case "DOWN": i = (0, 1)
            case "LEFT": i = (-1, 0)
            case "RIGHT": i = (1, 0)
            case _: assert(False)
        super().__init__(*i)

    def __repr__(self):
        return self.name



class beam:
    def __init__(self, beam_pos: tuple[int, int], beam_dir: str):
        self.pos = vector(*beam_pos)
        self.dir = direction(beam_dir)
    
    def __eq__(self, other: beam):
        return (self.pos == other.pos) and (self.dir == other.dir)

    def is_in_list(self, l: list[beam]):
        for other in l:
            if self == other:
                return True
        return False
    
    def __repr__(self):
        return str(self.pos) + ' ' + str(self.dir)