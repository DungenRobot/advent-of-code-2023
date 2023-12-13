
def is_symbol(char: str) -> bool:
    if char == '.' or char.isnumeric():
        return False
    else:
        return True


def check_for_symbol(number, grid, x, y) -> bool:
    
    length = len(number)

    left_x = max(0, x - length - 1)
    right_x = x


    min_y = 0
    max_y = len(grid) - 1

    x_values = range(left_x, right_x + 1)

    if y > min_y:
        for col in x_values:
            char = grid[y - 1][col]
            if is_symbol(char):
                return True
    
    if y < max_y:
        for col in x_values:
            char = grid[y + 1][col]
            if is_symbol(char):
                return True
    
    
    if is_symbol(grid[y][left_x]) or is_symbol(grid[y][right_x]):
        return True
    
    return False


def main():

    total = 0
    grid = []

    with open("input.txt") as f:
        for line in f.readlines():
            grid.append(line.strip() + '.')

    for y in range(len(grid)):
        current_number = ''

        for x in range(len(grid[0])):
            value: str = grid[y][x]
            print(value, end='')

            if value.isnumeric(): 
                current_number += value
            else:
                if current_number == '': continue

                is_adjacent = check_for_symbol(current_number, grid, x, y)
                if is_adjacent:
                    total += int(current_number)

                current_number = ''
        print()
            
    print(total)


if __name__ == "__main__":
    main()
    