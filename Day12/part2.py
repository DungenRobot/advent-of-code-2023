
cache = {}

def num_possible(row: str, key: list[int]) -> int:
    row = row.strip('.')

    cache_key = row + str(key)
    get = cache.get(cache_key)
    if get != None:
        return get

    if key == []:
        if '#' in row:
            return 0
        return 1
    if row == '':
        return 0
    
    first_chunk = row
    rest = ''
    if '.' in row:
        first_chunk, rest = row.split('.', 1)
    if set(first_chunk) == {'#'}:
        if len(first_chunk) == key[0]:
            out = num_possible(rest, key[1:])
            cache[cache_key] = out
            return out
        else:
            cache[cache_key] = 0
            return 0

    start, end = row.split('?', 1)

    str1 = start + '.' + end
    str2 = start + '#' + end

    out = num_possible(str1, key) + num_possible(str2, key)
    cache[cache_key] = out
    return out


def main():

    total = 0
    line_count = 0

    with open("input.txt") as f:
        for line in f.readlines():
            line = line.strip()

            row, key = line.split(' ')
            row = '?'.join([row] * 5)
            key = [int(num) for num in key.split(',')] * 5

            total += num_possible(row, key)

            line_count += 1
    print(total)
    print(len(cache.keys()))


if __name__ == "__main__":
    main()