from day1 import generate_maps, rotate, print_map

def find_horizontal_reflection(rock_map: list[str], stop_at_first: bool = False) -> list[int]:
    out = []
    max = len(rock_map) - 1
    for row_number in range(1, len(rock_map)):
        if rock_map[row_number - 1] == rock_map[row_number]:
            is_valid = True
            for i in range(0, row_number):
                other = (2 * row_number) - i - 1
                if other > max: continue
                if rock_map[i] != rock_map[other]:
                    is_valid = False
                    break
            if is_valid:
                out.append(i + 1)
                if stop_at_first: return out
    return out


def find_reflections(rock_map: list[str], stop_at_first: bool = False) -> tuple[list, list]:
    horizontal = find_horizontal_reflection(rock_map, stop_at_first)
    rock_map_flip = rotate(rock_map)
    #print_map(rock_map_flip)
    vertical = find_horizontal_reflection(rock_map_flip, stop_at_first)
    #print(vertical)
    return (horizontal, vertical)


def score_and_fix(rock_map: list[str]) -> int:

    h0, v0 = find_reflections(rock_map, True)
    #print(h0, v0)

    for row in range(len(rock_map)):
        for colm in range(len(rock_map[0])):
            i = rock_map[row][colm]
            old = rock_map[row]
            if i == '.': i = '#'
            elif i == '#': i = '.'

            rock_map[row] = rock_map[row][:colm] + i + rock_map[row][colm + 1:]

            h1, v1 = find_reflections(rock_map)

            if (h1 != []) or (v1 != []):
                for x in h1:
                    if x not in h0:
                        return x * 100
                for y in v1:
                    if y not in v0:
                        return y
            rock_map[row] = old
    return 0



def main():
    maps = generate_maps("input.txt")
    total = 0
    for rock_map in maps:
        total += score_and_fix(rock_map)
    
    print(total)




if __name__ == "__main__":
    main()
