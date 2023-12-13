
def generate_map(filesystem) -> dict:
    node_map = {}
    for line in filesystem.readlines():
        node = line[0:3]
        left = line[7:10]
        right = line[12:15]

        node_map[node] = [left, right]
    return node_map


def main():

    directions: str
    network = {}

    with open("input.txt") as f:
        directions = f.readline().strip()
        directions = directions.replace('L', '0')
        directions = directions.replace('R', '1')
        f.readline()

        network = generate_map(f)
    
    total_moves = 0
    current_node = "AAA"
    
    index = 0

    while current_node != "ZZZ":
        total_moves += 1
        move = int(directions[index])

        current_node = network[current_node][move]

        index += 1
        if index >= len(directions):
            index = 0

    print(total_moves)


if __name__ == "__main__":
    main()

