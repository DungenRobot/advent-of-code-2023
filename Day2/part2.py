from part1 import parse_grab

def main():
    total = 0

    with open('input.txt') as f:
        for line in f.readlines():
            line = line.split(': ')[1].strip()

            red = 0
            green = 0
            blue = 0
            
            for grab in line.split("; "):

                n_red, n_green, n_blue = parse_grab(grab)

                red = max(n_red, red)
                green = max(n_green, green)
                blue = max(n_blue, blue)

            power = red * green * blue

            total += power


        print(total)

if __name__ == "__main__": 
    main()

