
def get_gears(number, grid, x, y):
    gears_found = []

    length = len(number)

    left_x = max(0, x - length - 1)
    right_x = x

    min_y = 0
    max_y = len(grid) - 1

    x_values = range(left_x, right_x + 1)

    if y > min_y:
        for col in x_values:
            char = grid[y - 1][col]
            if char == '*':
                gears_found.append([y -1, col])
    
    if y < max_y:
        for col in x_values:
            char = grid[y + 1][col]
            if char == '*':
                gears_found.append([y + 1, col])
    
    if grid[y][left_x] == '*':
        gears_found.append([y, left_x])

    if grid[y][right_x] == '*':
        gears_found.append([y, right_x])
    
    return gears_found

def add_gear(gear_pos, number):
    gear_pos = str(gear_pos)
    
    if gear_pos in gear_dict.keys():
        gear_dict[gear_pos].append(number)
    else:
        gear_dict[gear_pos] = [number]

gear_dict = {}


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
            #print(value, end='')

            if value.isnumeric(): 
                current_number += value
            else:
                if current_number == '': continue

                adjacent_gears = get_gears(current_number, grid, x, y)

                for gear in adjacent_gears:
                    add_gear(gear, int(current_number))

                current_number = ''
        
    for gear in gear_dict.keys():

        if len(gear_dict[gear]) == 2:
            total += gear_dict[gear][0] * gear_dict[gear][1]
            
            
    print(total)


if __name__ == "__main__":
    main()