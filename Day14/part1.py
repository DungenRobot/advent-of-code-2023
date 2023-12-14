
def generate_map(path: str) -> list[list[str]]:
    out = []
    with open(path) as f:
        for line in f.readlines():
            line = line.strip()
            row = [char for char in line]
            out.append(row)
    return out


def shift_north(rock_map):
    for row_num in range(len(rock_map)):
        for colm_num in range(len(rock_map[0])):
            if rock_map[row_num][colm_num] != 'O':
                continue
            #if char == 'O':
            rock_map[row_num][colm_num] = '.'

            y = row_num

            while y - 1 >= 0:
                if rock_map[y - 1][colm_num] != '.':
                    break
                y -= 1
            
            rock_map[y][colm_num] = 'O'


def print_map(rock_map: list[list[str]]):
    for row in rock_map:
        for char in row:
            print(char, end='')
        print()
    print()


def main():
    rock_map = generate_map("input.txt")

    shift_north(rock_map)

    total = 0

    for row_num, row in enumerate(rock_map):
        score = len(rock_map) - row_num
        for char in row:
            if char == 'O':
                total += score
    print(total)


if __name__ == "__main__":
    main()
