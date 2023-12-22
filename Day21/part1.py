
STARTING_POSITION = 'S'
PLOT = '.'
ROCK = '#'
directions = [
    ( 1,  0),
    (-1,  0),
    ( 0, -1),
    ( 0,  1),
]
explored = set()
distances = {}

def generate_map(path):
    output_map: list[list[str]] = []
    start: list[int] = []
    with open(path) as f:
        row = -1
        for line in f.readlines():
            row += 1
            if STARTING_POSITION in line:
                start = (row, line.find(STARTING_POSITION))
            output_map.append([s for s in line.strip()])
    return (start, output_map)


def walk(pos, garden_map, steps: int = 64) -> set[tuple[int, int]]:
    row_max = len(garden_map)
    col_max = len(garden_map[0])

    if steps == 0: return

    row, col = pos

    for dr in directions:
        new_row = row + dr[0]
        new_col = col + dr[1]
        #print(new_row, new_col, steps)
        if not ((0 <= new_row < row_max) and (0 <= new_col < col_max)): continue
        if garden_map[new_row][new_col] == ROCK: continue
        new = (new_row, new_col)
        if new in explored: 
            if distances[new] >= steps: continue
        #print("valid\n")
        explored.add(new)
        distances[new] = steps
        walk(new, garden_map, steps - 1)


def print_garden(garden):
    for row in range(len(garden)):
        for col in range(len(garden[0])):
            pos = (row, col)
            if pos in explored:
                print('O', end='')
            else:
                print(garden[row][col], end='')
        print()


def main():
    start, garden = generate_map("input.txt")
    steps = 64
    walk(start, garden, steps)

    start_i = (start[0] + start[1]) % 2

    total = 0
    for pos in explored.copy():
        if ((pos[0] + pos[1]) % 2) == start_i:
            total += 1
        else:
            explored.remove(pos)

    print(total)
    #print_garden(garden)
    print(len(explored))


if __name__ == "__main__":
    main()
