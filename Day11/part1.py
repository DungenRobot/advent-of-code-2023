
def generate_star_map(path: str) -> list[list[int]]:
    star_map = []
    with open(path) as f:
        for line in f.readlines():
            line = line.strip()
            star_map.append([char for char in line])
    return star_map


def get_empty_rows(star_map: list) -> list[int]:
    empty_rows = []
    for row_number, row in enumerate(star_map):
        if row == ['.'] * len(row):
            empty_rows.append(row_number)
    return empty_rows


def get_empty_columns(star_map: list) -> list[int]:
    empty_columns = []
    for colm in range(len(star_map[0])):
        filled = [True for x in star_map if x[colm] != '.']
        is_empty = (filled == [])
        if is_empty:
            empty_columns.append(colm)
    return empty_columns


def get_galaxies(star_map: list) -> list[tuple[int, int]]:
    galaxies = []
    for row_number, row in enumerate(star_map):
        for colm_number, i in enumerate(row):
            if i == '#':
                galaxies.append((row_number, colm_number))
    return galaxies


def get_distance(galaxy1: tuple[int, int], galaxy2: tuple[int, int], empty_rows: list[int], empty_columns: list[int]):
    gr1, gc1 = galaxy1
    gr2, gc2 = galaxy2

    if gr1 > gr2:
        gr1, gr2 = gr2, gr1
    if gc1 > gc2:
        gc1, gc2 = gc2, gc1

    middle_rows = range(gr1 + 1, gr2)
    middle_colms = range(gc1 + 1, gc2)

    row_padding = len([1 for row in middle_rows if row in empty_rows])
    colm_padding = len([1 for colm in middle_colms if colm in empty_columns])

    return (gr2 - gr1) + (gc2 - gc1) + row_padding + colm_padding


def main():

    #initialize star map
    star_map = generate_star_map("input.txt")
    galaxies = get_galaxies(star_map)

    empty_rows = get_empty_rows(star_map)
    empty_columns = get_empty_columns(star_map)

    total = 0

    while galaxies != []:
        g = galaxies.pop()

        for other in galaxies:
            total += get_distance(g, other, empty_rows, empty_columns)
    
    print(total)




    




if __name__ == "__main__":
    main()