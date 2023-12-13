
def make_solutions(row: str) -> list:
    if '?' not in row:
        return [row]

    solutions = []
    start, end = row.split('?', 1)

    new_1 = start + '.' + end
    new_2 = start + '#' + end

    return make_solutions(new_1) + make_solutions(new_2)


def check_solutions(solutions: list[str], key: list[int]) -> int:
    total = 0
    for row in solutions:
        chunks = [len(chunk) for chunk in row.split('.') if len(chunk) != 0]
        if chunks == key:
            total += 1
    return total


def main():

    total = 0

    with open("test.txt") as f:
        for line in f.readlines():
            line = line.strip()
        
            row, key = line.split(' ')
            key = [int(num) for num in key.split(',')]

            solutions = make_solutions(row)
            total += check_solutions(solutions, key)
    print(total)


if __name__ == "__main__":
    main()
