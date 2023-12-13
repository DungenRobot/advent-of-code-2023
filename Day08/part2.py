from part1 import generate_map
import math


def main():
    directions: str
    network = {}

    with open("input.txt") as f:
        directions = f.readline().strip()
        directions = directions.replace('L', '0')
        directions = directions.replace('R', '1')
        f.readline()

        network = generate_map(f)

    node_list = []
    for node in network:
        node: str
        if node.endswith('A'): node_list.append(node)

    total_moves = 0
    index = 0

    loop_counts = []

    while len(node_list) != 0:
        total_moves += 1
        move = int(directions[index])

        node_list = [network[node][move] for node in node_list]

        for node in node_list:
            if node.endswith('Z'):
                loop_counts.append(total_moves)
                node_list.remove(node)

        if total_moves % 1_000_000 == 0: print(total_moves)
        
        index += 1
        if index >= len(directions):
            index = 0
        
    print(math.lcm(*loop_counts))

    print(total_moves)

if __name__ == "__main__":
    main()
    