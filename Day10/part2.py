from utility import vector as position
from utility import UP, DOWN, LEFT, RIGHT, array_directions


def generate_map(file_path: str):
    pipe_map = []
    with open(file_path) as f:
        for line in f.readlines():
            line = line.strip()
            pipe_map.insert(0, line)
    return pipe_map


dir_left = {
    str(LEFT) : DOWN,
    str(DOWN) : RIGHT,
    str(RIGHT) : UP,
    str(UP) : LEFT,
}


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

def print_map_with_marks(pipe_map: list, marks: list):
    for y in range(len(pipe_map)):
        y = len(pipe_map) - y - 1
        for x in range(len(pipe_map[0])):
            pos = position(x, y)
            if pos in marks:
                print("I", end='')
            else:
                print(pipe_map[y][x], end='')
        print()
            
        

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

    steps = []
    last_dir = position(0, 0)

    while (current_pos != start_pos ):
        difference = current_pos - last_pos
        pipe = pipe_map[current_pos.y][current_pos.x]
        next_pos = get_next_pos(difference, pipe) + current_pos
        steps.append([current_pos, difference])

        if last_dir != difference:
            steps.append([last_pos, difference])

        last_pos = current_pos
        current_pos = next_pos
        last_dir = difference
    
    all_pos = [p[0] for p in steps]
    
    inside = []

    for pos, dir in steps:

        new_pos = pos + dir

        dir_in = dir_left[str(dir)]

        new_pos = pos + dir_in

        while new_pos not in all_pos:
            inside.append(new_pos)
            new_pos += dir_in
    print_map_with_marks(pipe_map, inside)

    unique = []

    total = 0

    for i in range(len(inside)):
        pos = inside[i]
        is_unique = True
        print(pos)
        for x in range(i + 1, len(inside)):
            if pos == inside[x]:
                print(inside[x])
                print()
                is_unique = False
                break
        if is_unique:
            total += 1
            unique.append(pos)
    
        
    print(total)

    

if __name__ == "__main__":
    main()
