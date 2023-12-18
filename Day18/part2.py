
dig_shape: list[tuple[tuple[int, int], tuple[int, int]]] = []

boundary: int = int(0)

directions = [
    [ 0,  1],
    [ 1,  0],
    [ 0, -1],
    [-1,  0],
]

def generate_shape(path: str):
    pos = [0, 0]
    with open(path) as f:
        for line in f.readlines():
            point = (pos[0], pos[1])
            dig_shape.append(point)

            hex = line.split()[-1]

            length = int(hex[2:-2], 16)
            global boundary
            boundary += length
            dir = int(hex[-2])
            dir = directions[dir]

            new = [(v * length) for v in dir]
            new[0] += pos[0]
            new[1] += pos[1]
            pos = new


def get_num_inside(l):
    area = 0
    for i in range(0, len(l) - 1):
        pi = l[i]
        pi_one = l[i+1]
        area += (pi[1] * pi_one[0]) - (pi_one[1] * pi[0])
    first = l[0]
    last = l[-1]
    area += (last[1] * first[0]) - (first[1] * last[0])
    return area // 2

def get_area():
    interior = get_num_inside(dig_shape)
    return interior + (boundary // 2) + 1

def main():
    generate_shape("input.txt")
    print(get_area())
    print(get_area() - 952408144115)

if __name__ == "__main__":
    main()
    