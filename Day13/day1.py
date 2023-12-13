

def generate_map(path: str) -> list[list[str]]:
    map_out = []
    with open(path) as f:
        for line in f.readlines():
            map_out.append()
    return map_out


def main():
    rock_map = generate_map("test.txt")

    pass

if __name__ == "__main__":
    main()