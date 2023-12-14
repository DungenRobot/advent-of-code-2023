
def generate_maps(path: str) -> list[list[str]]:
    maps = []
    current_map = []
    with open(path) as f:
        for line in f.readlines():
            line = line.strip()
            if line == '':
                maps.append(current_map)
                current_map = []
            else:
                current_map.append(line)
        maps.append(current_map)
    return maps


def score_map(rock_map: list[str]):
    last_line = ''
    line_number = 0

    for i in range(len(rock_map) - 1):
        if (rock_map[i] == rock_map[i + 1]) and is_horizontal_reflection(rock_map, i):
            return i + 1
    
    return 0


def is_horizontal_reflection(rock_map: list[str], i: int):
    max = len(rock_map) - 1
    min = 0

    for row_num in range(0, i):
        diff = i - row_num  + 1
        if i + diff > max:
            continue
        #print(row_num, i + diff)
        #print(rock_map[row_num], rock_map[i+ diff])
        if rock_map[row_num] != rock_map[i + diff]:
            return False
    
    return True


def rotate(rock_map: list[str]) -> list[str]:
    map_out = []
    new = [row for row in rock_map]
    for char in new.pop(0):
        map_out.append(char)

    for row in new:
        for i, char in enumerate(row):
            map_out[i] += char
    
    return map_out


def print_map(rock_map):
    for row in rock_map:
        print(row)


def main():
    maps = generate_maps("input.txt")

    total = 0

    for rock_map in maps:
        total += score_map(rock_map) * 100
        total += score_map(rotate(rock_map))
    
    print(total)

if __name__ == "__main__":
    main()
