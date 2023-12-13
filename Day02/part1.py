max_red = 12
max_green = 13
max_blue = 14

def parse_grab(grab):
    t = {
        "red" : 0,
        "green" : 0,
        "blue" : 0
    }

    for i in grab.split(", "):
        number, color = i.split(" ")
        t[color] += int(number)

    return (t['red'], t['green'], t['blue'])

def test_grab(grab):
    red, green, blue = parse_grab(grab)
    if (red > max_red) or (green > max_green) or (blue > max_blue):
        return 1
    return 0

def main():
    total = 0
    with open("input.txt") as f:
        for line in f.readlines():
            line = line[5:].strip()
            id, line = line.split(': ')
            id = int(id)

            test = [test_grab(grab) for grab in line.split("; ")]

            if sum(test) == 0: total += id
    print(total)

if __name__ == "__main__":
    main()