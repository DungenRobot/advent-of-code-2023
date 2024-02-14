from __future__ import annotations


class Vector:
    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z
    
    def __repr__(self):
        return str((self.x, self.y, self.z))
    
    def __hash__(self):
        return hash(str(self))
    
    def __eq__(self, other: Vector):
        return (self.x == other.x) and (self.y == other.y) and (self.z == other.z) 


class Ray:
    def __init__(self, origin: tuple[int, int, int], dir: tuple[int, int, int]):
        self.origin = Vector(*origin)
        self.dir = Vector(*dir)
        self.slope = (self.dir.y / self.dir.x)

    def __repr__(self):
        return str(self.origin) + str(self.dir)

    def __hash__(self):
        return hash(str(self))

    def __eq__(self, other: Ray):
        return (self.origin == other.origin) and (self.dir == other.dir)
    

    def get_t_from_x(self, x):
        return (x - self.origin.x) / self.dir.x


    def collides_with_2D(self, other: Ray): 
        lb = 200000000000000 #lower bound
        ub = 400000000000000 #upper bound

        denom = (self.dir.y * other.dir.x) - (self.dir.x * other.dir.y)
        if denom == 0: return False

        p1 = (self.dir.x * other.dir.x) * (other.origin.y - self.origin.y)
        p2 = self.dir.y * other.dir.x * self.origin.x
        p3 = self.dir.x * other.dir.y * other.origin.x

        x = (p1 + p2 - p3) / denom

        if not (lb <= x <= ub): return False

        y = self.slope * (x - self.origin.x) + self.origin.y

        if not (lb <= y <= ub): return False

        if self.get_t_from_x(x) < 0: return False
        if other.get_t_from_x(x) < 0: return False

        return True

def generate_ray_set(path: str) -> set[Ray]:
    out = set()
    with open(path) as f:
        for line in f.readlines():
            origin_str, dir_str = line.split(' @ ')
            origin: tuple = [int(i) for i in origin_str.split(', ')]
            dir: tuple = [int(i) for i in dir_str.split(', ')]
            r = Ray(origin, dir)
            out.add(r)
    return out


def check_path_collisions(s: set[Ray]) -> int:
    total = 0
    while len(s) > 1:
        r_1 = s.pop()
        for r_2 in s:
            if r_1.collides_with_2D(r_2): total += 1
    return total


def main():
    s = generate_ray_set("input.txt")
    print(check_path_collisions(s))

if __name__ == "__main__":
    main()