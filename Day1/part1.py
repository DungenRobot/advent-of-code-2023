

with open("input.txt") as f:
    total = 0
    for line in f.readlines():
        first = -1
        last = 0
        for char in line:
            try:
                char = int(char)
                if first == -1: first = char
                last = char
            except:
                continue
        total += (first * 10) + last
    print(total)

