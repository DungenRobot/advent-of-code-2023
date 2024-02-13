from part1 import generate_map, find_nodes

directions = [
    [ 0,  1],
    [ 0, -1],
    [ 1,  0],
    [-1,  0],
]

def get_pos_around(pos: tuple[int, int]) -> list[tuple[int, int]]:
    """
    Given a position (in the form of a tuple), return all the positions around it (as a list)
    """
    out = []
    row, col = pos
    for i, j in directions:
        out.append((row + i, col + j))
    return out


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
        moves.append(m)
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

    for node in graph:
        if end_node in graph[node].keys():
            graph[end_node] = {node: graph[node][end_node]}

    return (end_node, graph)


def get_longest_path(graph: dict[tuple[int, int], dict], end_node: tuple[int, int], current: tuple[int, int] = (1,1), history: set[tuple[int, int]] = set(), distance: int = 0):

    if current == end_node: return distance
    history.add(current)

    most = -1

    for next in graph[current]:
        if next in  history: continue
        h = history.copy()
        h.add(current)
        d = distance + graph[current][next]
        i = get_longest_path(graph, end_node, next, h, d)
        most = max(most, i)
    
    return most


def main():
    trail_map = generate_map("input.txt")
    nodes = find_nodes(trail_map)

    end_node, graph = create_graph(nodes, trail_map)

    print(get_longest_path(graph, end_node) + 1)



if __name__ == "__main__":
    main()