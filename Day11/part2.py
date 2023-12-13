from part2 import generate_star_map, get_empty_rows, get_empty_columns, get_galaxies

def get_distance(galaxy1: tuple[int, int], galaxy2: tuple[int, int], empty_rows: list, empty_columns: list):
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

    return (gr2 - gr1) + (gc2 - gc1) + (row_padding * 999_999) + (colm_padding * 999_999)


def main():

    #initialize star map
    star_map = generate_star_map("input.txt")
    galaxies: list = get_galaxies(star_map)

    empty_rows = get_empty_rows(star_map)
    empty_columns = get_empty_columns(star_map)

    total = 0

    while galaxies != []:
        g = galaxies.pop()

        for other in galaxies:
            total += get_distance(g, other, empty_rows, empty_columns)

if __name__ == "__main__":
    main()
    