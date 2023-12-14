from part1 import shift_north, generate_map, print_map


def make_str(rock_map: list[list[str]]) -> str:
    return ''.join([''.join(row) for row in rock_map])


def rotate_map(rock_map: list[list[str]]) -> [list[list[str]]]:
    out = []
    for colm in range(len(rock_map[0])):
        new_row = []
        for row in range(len(rock_map), 0, -1):
            new_row.append(rock_map[row - 1][colm])
        out.append(new_row)
    return out


def do_iteration(rock_map: [list[list[str]]]) -> list[list[str]]:
    for _ in range(4):
        shift_north(rock_map)
        rock_map = rotate_map(rock_map)
    return rock_map


def score_map(rock_map: list[list[str]]) -> int:
    total = 0
    for row_num, row in enumerate(rock_map):
        score = len(rock_map) - row_num
        for char in row:
            if char == 'O':
                total += score
    return total


def main():
    past_boards = {}

    rock_map = generate_map("input.txt")

    iteration_number = 0
    start_loop = 0

    while True:
        rock_map = do_iteration(rock_map)
        iteration_number += 1

        key = make_str(rock_map)

        if key in past_boards.keys():
            start_loop = past_boards[key]
            break
        else:
            past_boards[key] = iteration_number
    
    loop_size = iteration_number - start_loop

    target = ((1_000_000_000 - start_loop) % loop_size)

    iteration_number = 0

    while iteration_number != target:
        rock_map = do_iteration(rock_map)
        iteration_number += 1
        
    print(score_map(rock_map))


if __name__ == "__main__":
    main()
