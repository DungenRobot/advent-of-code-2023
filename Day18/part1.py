
dig_map: set[tuple[int, int]] = {(0, 0)}

directions = {
    'U' : [-1,  0],
    'R' : [ 0,  1],
    'D' : [ 1,  0],
    'L' : [ 0, -1],
}

bounds = [0, 0, 0, 0]

def generate_map(path: str):
    pos = [0, 0]
    with open(path) as f:
        for line in f.readlines():
            dir, i, _ = line.split()
            i = int(i)
            dir = directions[dir]

            for _ in range(i):
                pos[0] += dir[0]
                pos[1] += dir[1]
                expand_bounds(*pos)

                data = (pos[0], pos[1])
                dig_map.add(data)


def expand_bounds(row, col):
    bounds[0] = min(bounds[0], row)
    bounds[2] = max(bounds[2], row + 1)
    bounds[1] = max(bounds[1], col + 1)
    bounds[3] = min(bounds[3], col)


def dig_hole():
    #flood fill
    top, right, bottom, left = bounds

    middle_row = top + (bottom - top) // 2
    middle_col = left + (right - left) // 2

    unexplored = {(middle_row, middle_col)}

    while len(unexplored) != 0:
        pos = unexplored.pop()
        dig_map.add(pos)
        
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                new_pos = [*pos]
                new_pos[0] += i
                new_pos[1] += j

                new_pos = (new_pos[0], new_pos[1])
                if new_pos in dig_map:
                    continue
                unexplored.add(new_pos)


def main():
    generate_map("input.txt")
    dig_hole()
    print(len(dig_map))

if __name__ == "__main__":
    main()
    