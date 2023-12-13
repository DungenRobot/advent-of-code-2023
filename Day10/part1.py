from utility import vector as position
from utility import UP, DOWN, LEFT, RIGHT, array_directions


def generate_map(file_path: str):
    pipe_map = []
    with open(file_path) as f:
        for line in f.readlines():
            line = line.strip()
            pipe_map.insert(0, line)
    return pipe_map


pipe_dict = {
    '|' : [UP, DOWN],
    '-' : [LEFT, RIGHT],
    'L' : [DOWN, LEFT],
    'J' : [DOWN, RIGHT],
    '7' : [RIGHT, UP],
    'F' : [UP, LEFT],
}


def print_map(pipe_map: list):
    for i in range(len(pipe_map)):
        i = len(pipe_map) - i - 1
        print(''.join(pipe_map[i]))

def find_start_pos(map: list) -> position:
    for y in range(len(map)):
        if 'S' in map[y]:
            return position(map[y].find('S'), y)

def find_start_pipe(map: list, start_pos: position):
    for direction in array_directions:
        pos = start_pos + direction
        pipe = map[pos.y][pos.x]
        if pipe == '.': continue
        if direction in pipe_dict[pipe]:
            return pos


def get_next_pos(difference: position, pipe: str) -> tuple:
    """
    Takes in the difference from the last move to the current move
    (current_pos - last_pos) and the type of pipe
    Returns a the position of the next move
    """
    pipe_paths = pipe_dict[pipe]

    if pipe_paths[0] == difference:
        return -pipe_paths[1]
    else:
        return -pipe_paths[0]


def main():
    pipe_map = generate_map("input.txt")

    print_map(pipe_map)

    start_pos = find_start_pos(pipe_map)
    last_pos = start_pos
    current_pos = find_start_pipe(pipe_map, start_pos)

    print(start_pos)
    print(current_pos)

    steps = 1

    while (current_pos != start_pos ):
        difference = current_pos - last_pos
        pipe = pipe_map[current_pos.y][current_pos.x]
        next_pos = get_next_pos(difference, pipe) + current_pos
        steps += 1

        last_pos = current_pos
        current_pos = next_pos

    print(steps // 2)

if __name__ == "__main__":
    main()
