import bisect

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
    global explored
    global distances

    unexplored = [pos]
    next_to_explore = []

    row_max = len(garden_map)
    col_max = len(garden_map[0])

    for _ in range(steps):
        while len(unexplored) > 0:
            row, col = unexplored.pop()
            for dr in directions:
                    new_row = row + dr[0]
                    new_col = col + dr[1]
                    if garden_map[new_row % row_max][new_col % col_max] == ROCK: continue
                    new = (new_row, new_col)
                    if new in explored: 
                        if distances[new] >= steps: continue
                    next_to_explore.append(new)
                    explored.add(new)
                    distances[new] = steps
        unexplored = next_to_explore
        next_to_explore = []


def count_parity(positions, start, steps):
    start_i = (start[0] + start[1] + steps) % 2
    total = 0
    for pos in positions:
        if ((pos[0] + pos[1]) % 2) == start_i:
            total += 1
    return total


def main():
    start, garden = generate_map("input.txt")
    gridlength = 65 + len(garden[0]) * 2
    steps = gridlength
    walk(start, garden, steps)

    total = count_parity(explored, start, steps)

    print(gridlength, total)


if __name__ == "__main__":
    main()
    x = 202300
    print(3893 + (15495 * x) + ( 15397 * x * x))
    #print((26501365 - 65)/131)