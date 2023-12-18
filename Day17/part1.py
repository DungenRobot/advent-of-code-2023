from __future__ import annotations
import bisect


directions: dict[str, list[int]] = {
    'N' : [-1,  0],
    'E' : [ 0,  1],
    'S' : [ 1,  0],
    'W' : [ 0, -1],
}

reverse: dict[str, str] = {
    'N' : 'S',
    'E' : 'W',
    'S' : 'N',
    'W' : 'E',
}

heat_map = []
target = [0, 0]

def generate_map(path: str):
    with open(path) as f:
        for line in f.readlines():
            heat_map.append([int(char) for char in line.strip()])
    target[0] = len(heat_map) - 1
    target[1] = len(heat_map[0]) - 1


def generate_neighbors(row, col, history):
    out = []
    for dir_name in directions:
        last_dir, streak = history
        
        if reverse[dir_name] == last_dir: continue
        if (dir_name == last_dir) and streak >= 3: continue

        dir = directions[dir_name]
        new_pos = (row + dir[0], col + dir[1])
        inside_grid = (0 <= new_pos[0] < len(heat_map)) and (0 <= new_pos[1] < len(heat_map[0]))
        if not inside_grid: continue
        out.append((dir_name, new_pos))
    return out


def main():
    generate_map("input.txt")

    searched = set()
    unsearched = [(0, 0, ('_', 0), 0)]

    minimum_heat = 0

    while unsearched != []:
        row, col, history, heat_loss = unsearched.pop(0)

        if [row, col] == target: 
            minimum_heat = (heat_loss, history)
            break

        for pair in generate_neighbors(row, col, history):
            dir_name, neighbor_pos = pair
            last_dir, streak = history

            new_history: tuple[str, int]
            if last_dir == dir_name:
                new_history = (dir_name, streak + 1)
            else:
                new_history = (dir_name, 1)

            key = (neighbor_pos, new_history)
            if key in searched: continue
            searched.add(key)

            cost = heat_map[neighbor_pos[0]][neighbor_pos[1]]
            new_state = (neighbor_pos[0], neighbor_pos[1], new_history, heat_loss + cost)
            bisect.insort(unsearched, new_state, key=lambda x: x[3])
    
    print(minimum_heat)


if __name__ == "__main__":
    main()
