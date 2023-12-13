
def generate_maps(path: str) -> list[list[str]]:
    maps = []
    current_map = []
    with open(path) as f:
        for line in f.readlines():
            if line == '':
                maps.append(current_map)
                current_map = []
            else:
                current_map.append(line)
    return maps


def main():
    rock_map = generate_map("test.txt")

    pass

if __name__ == "__main__":
    main()