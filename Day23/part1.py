
directions = [
    [ 0,  1],
    [ 0, -1],
    [ 1,  0],
    [-1,  0],
]


def generate_map(path: str) -> list[list[str]]:
    """
    Takes in a file path and returns a 2D list of characters
    """
    trail_map = []
    with open(path) as f:
        for line in f.readlines():
            trail_map.append([char for char in line.strip()])
    return trail_map


def get_pos_around(pos: tuple[int, int]) -> list[tuple[int, int]]:
    """
    Given a position (in the form of a tuple), return all the positions around it (as a list)
    """
    out = []
    row, col = pos
    for i, j in directions:
        out.append((row + i, col + j))
    return out


def find_nodes(trail_map: list[list[str]]) -> set[tuple[int, int]]:
    """
    Find every position where we can make a choice on the map
    """
    nodes = {(1, 1)}
    for row in range(1, len(trail_map) - 1):
        for col in range(1, len(trail_map[0]) - 1):
            if trail_map[row][col] != '.': continue
            num_directions = 0
            for row_i, col_i in get_pos_around((row, col)):
                if trail_map[row_i][col_i] != '#': num_directions += 1
            if num_directions > 2: nodes.add((row, col))
    return nodes

invalid = {
    '^': [ 0,  1], 
    'v': [ 0, -1],
    '<': [ 1,  0],
    '>': [-1,  0],
    '.': [      ],
}

def generate_valid_moves(pos, last_pos, trail_map):
    """
    Generate all the moves around the user that are valid
    """
    moves = []
    for m in get_pos_around(pos):
        delta = [m[1] - pos[1], m[0] - pos[0]]
        if m == last_pos: continue
        tile = trail_map[m[0]][m[1]]
        if tile == '#': continue
        #print(tile)
        if invalid[tile] == delta: continue
        moves.append(m)
    #if len(moves) > 1: print(moves)
    return moves


def create_graph(nodes: set[tuple[int, int]], trail_map):
    graph: dict[tuple[int, int], dict[tuple[int, int], int]] = {}
    end_node = (len(trail_map) -1, len(trail_map[0]) - 2)
    nodes.add(end_node)

    for node in nodes:
        if node == end_node: continue
        pos = node_pos = node

        some_data = graph.get(pos, {})

        for start_pos in generate_valid_moves(pos, node_pos, trail_map):
            last_pos = node_pos
            pos = start_pos
            distance = 1

            while True:
                distance += 1
                pos, last_pos = generate_valid_moves(pos, last_pos, trail_map)[0], pos
                if pos in nodes:
                    break
            some_data[pos] = distance
        graph[node_pos] = some_data
    
    graph[end_node] = {}

    return (end_node, graph)

def get_longest_path(graph: dict[tuple[int, int], dict], end_node):

    distances = {}
    for node in graph:
        distances[node] = 0

    no_parents = [end_node]

    while len(no_parents) > 0:
        node = no_parents.pop()

        if node == (1, 1): return distances[node] + 1

        for other in graph: 
            if node not in graph[other].keys(): continue
            parent = other

            distance_2_parent = graph[parent].pop(node) + distances[node]
            distances[parent] = max(distance_2_parent, distances[parent])
            
            if len(graph[parent].keys()) == 0:
                no_parents.append(parent)


def main():
    trail_map = generate_map("input.txt")
    nodes = find_nodes(trail_map)
    end_node, graph = create_graph(nodes, trail_map)
    print(get_longest_path(graph, end_node))

if __name__ == "__main__":
    main()