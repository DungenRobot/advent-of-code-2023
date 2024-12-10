import random

def add_edge(graph: dict[str, set[str]], node1: str, node2: str):
    graph[node1] = graph.get(node1, set())
    graph[node1].add(node2)
    graph[node2] = graph.get(node2, set())
    graph[node2].add(node1)


## Basic search algorithm
def get_shortest_path(graph: dict[str, set[str]], start: str, end: str) -> list[str]:

    scores: dict[str, int] = {end: 0}

    i = 0

    while start not in scores:
        neighbors = []

        for node in [n for n, score in scores.items() if score == i]:
            for node_neighbor in graph[node]:
                if not node_neighbor in scores:
                    neighbors.append(node_neighbor)

        i += 1
        
        for node in neighbors:
            scores[node] = i

    path = [start]

    while path[-1] != end:
        best_node = ""

        for node in graph[path[-1]]:
            if not node in scores:
                continue
            if scores[node] < scores.get(best_node, 1000000):
                best_node = node

        path.append(best_node)


    return path


def count_connected_nodes(graph: str, node: str) -> int:
    visited: set = set()
    upcoming: set = {node}

    while upcoming != set():
        next = upcoming.pop()
        visited.add(next)

        upcoming = upcoming.union([n for n in graph[next] if not n in visited])

    return len(visited)


def main():

    graph: dict[str, set[str]] = dict()

    #build graph
    with open("input") as f:
        for line in f:
            node, edges = line.strip().split(': ')
            for edge in edges.split(' '):
                add_edge(graph, node, edge)
    
    #create a heat map of edges
    edge_heat_map: dict[str, int] = {}

    graph_nodes = list(graph.keys())

    for _ in range(1000):
        start = random.choice(graph_nodes)
        end = random.choice(graph_nodes)
        
        path = get_shortest_path(graph, start, end)

        for i in range(len(path) - 1):
            pair = [path[i], path[i+1]]
            pair.sort()
            pair_string = pair[0] + '/' + pair[1]
            edge_heat_map[pair_string] = edge_heat_map.get(pair_string, 0) + 1

    #find the top three and remove them
    top_three = sorted(edge_heat_map.items(), key= lambda ele: -ele[1])[:3]
    
    for edge, _heat in top_three:
        node1, node2 = edge.split('/')

        graph[node1].remove(node2)
        graph[node2].remove(node1)

    #take any two nodes from a removed edge and count how many are connected
    node1, node2 = top_three[0][0].split('/')
    print(count_connected_nodes(graph, node1) * count_connected_nodes(graph, node2))



if __name__ == "__main__":
    main()