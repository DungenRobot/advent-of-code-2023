
def main():

    values = []
    modified = []

    f = open("input.txt")

    seeds = [int(i) for i in f.readline().removeprefix("seeds:").strip().split(' ')]

    modified = [False for x in seeds]
    f.readline()

    for line in f.readlines():
        line = line.strip()
        if line == "":
            continue
        if line.endswith(":"):
            modified = [False for x in seeds]
            print(seeds)
            print(line)
            continue

        destination, source, length = line.split(' ')
        destination, source, length = int(destination), int(source), int(length)

        for i in range(len(seeds)):
            if modified[i]:
                continue
            if (source <= seeds[i] < (source + length)):
                seeds[i] += destination - source
                modified[i] = True
    print(seeds)
    print(min(seeds))


if __name__ == "__main__":
    main()