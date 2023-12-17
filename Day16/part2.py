from utility import beam, direction, vector


def generate_map(path: str) -> list[list[str]]:
    out = []
    with open(path) as f:
        for line in f.readlines():
            out.append([char for char in line.strip()])
    return out


def print_map(m: list[list[str]]):
    for line in m:
        for char in line:
            print(char, end='')
        print()


def print_map(m: list[list[str]], positions: list[vector]):
    for y, line in enumerate(m):
        for x, char in enumerate(line):
            pos = vector(x, y)
            if pos.is_in_list(positions):
                print('#', end='')
            else:
                print(char, end='')
        print()


mirrors: dict[str, dict[str, list[str]]] = {
    '/' : {
        'UP': ['RIGHT'],
        'DOWN' : ['LEFT'],
        'LEFT' : ['DOWN'],
        'RIGHT' : ['UP'],
    },
    '\\' : {
        'UP': ['LEFT'],
        'DOWN' : ['RIGHT'],
        'LEFT' : ['UP'],
        'RIGHT' : ['DOWN'],
    },
    '|' : {
        'UP': ['UP'],
        'DOWN' : ['DOWN'],
        'LEFT' : ['UP', 'DOWN'],
        'RIGHT' : ['UP', 'DOWN'],
    },
    '-' : {
        'UP': ['LEFT', 'RIGHT'],
        'DOWN' : ['LEFT', 'RIGHT'],
        'LEFT' : ['LEFT'],
        'RIGHT' : ['RIGHT'],
    },
    '.' : {
        'UP': ['UP'],
        'DOWN' : ['DOWN'],
        'LEFT' : ['LEFT'],
        'RIGHT' : ['RIGHT'],
    }
}


def get_energy_value(initial_beam: beam, mirror_map: list[list[str]]):
    y_max = len(mirror_map)
    x_max = len(mirror_map[0])

    past_beams: list[beam] = []
    active_beams: list[beam] = [initial_beam]

    while active_beams != []:
        current_beam = active_beams.pop()
        if current_beam.is_in_list(past_beams): continue
        b_pos = current_beam.pos
        b_dir = current_beam.dir

        col, row = b_pos.x, b_pos.y
        mir = mirror_map[row][col]
        
        for dir_name in mirrors[mir][b_dir.name]:
            dir = direction(dir_name)
            new_pos = b_pos + dir
            if not new_pos.is_within_bounds(0, x_max, 0, y_max):
                continue
            new_beam = beam(new_pos.get_tuple(), dir.name)
            active_beams.append(new_beam)

        past_beams.append(current_beam)
        
    positions = []
    total = 0

    for b in past_beams:
        pos = b.pos
        if pos.is_in_list(positions):
            continue
        total += 1
        positions.append(pos)
    #print_map(mirror_map, positions)
    return total


def main():
    mirror_map = generate_map("input.txt")
    #print_map(mirror_map)
    max_energy = 0
    print(1)
    for x in range(len(mirror_map)):
        print(x)
        v = get_energy_value(beam((x, 0), 'DOWN'), mirror_map)
        max_energy = max(v, max_energy)
    print(2)
    for x in range(len(mirror_map[0])):
        print(x)
        v = get_energy_value(beam((x, len(mirror_map) - 1), 'UP'), mirror_map)
        max_energy = max(v, max_energy)
    print(3)
    for y in range(len(mirror_map)):
        print(x)
        v = get_energy_value(beam((0, y), 'RIGHT'), mirror_map)
        max_energy = max(v, max_energy)
    print(4)
    for y in range(len(mirror_map)):
        print(x)
        v = get_energy_value(beam((len(mirror_map[0]) - 1, y), 'LEFT'), mirror_map)
        max_energy = max(v, max_energy)
    
    print(max_energy)


if __name__ == "__main__":
    main()
