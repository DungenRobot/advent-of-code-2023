from part1 import get_falling, do_fall, find_supporting


def count_supporting(supporting: dict):
    #create a dict of form key: rect name and value: how many blocks support it
    counts = {}
    for supported in supporting.values():
        for s in supported:
            counts[s] = counts.get(s, 0) + 1
    return counts


def find_total_fall(supporting: dict[str, list[str]], counts: dict[str, int]):
    #there's probably a way to add a cache to this. I didn't bother
    total = 0

    for block in supporting:
        sub_total = -1
        c = counts.copy()
        fall_buffer = [block]

        while len(fall_buffer) != 0:
            current = fall_buffer.pop(0)
            sub_total += 1

            for supported in supporting[current]:
                c[supported] -= 1
                if c[supported] == 0:
                    fall_buffer.append(supported)
        print(block, sub_total)
        total += sub_total
    return total


def main():
    falling = get_falling("input.txt") #gets a list of all the rects in the air
    print("collected")
    stack = do_fall(falling) #makes them fall into a stack. Returns a named stack of rectangles
    print("fell")
    supporting = find_supporting(stack) #returns what rects are supporting what others
    print("checked")
    counts = count_supporting(supporting)

    total = find_total_fall(supporting, counts)

    print(total)


if __name__ == "__main__":
    main()