
def hash(line: str) -> int:
    current_value = 0
    for char in line:
        current_value += ord(char)
        current_value *= 17
    return current_value & 255


def main():
    instructions = []
    with open("input.txt") as f:
        instructions = f.readline().strip().split(',')
    
    total = 0
    for line in instructions:
        value = hash(line)
        total += value

    print(total)


if __name__ == "__main__":
    main()
