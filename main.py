from collections import defaultdict

def make_undirected_graph(edge_list):
    """ Makes an undirected graph from a list of edge tuples. """
    graph = defaultdict(set)
    for e in edge_list:
        graph[e[0]].add(e[1])
        graph[e[1]].add(e[0])
    return graph


def reachable(graph, start_node):
    """
    Returns:
      the set of nodes reachable from start_node
    """
    result = set([start_node])
    frontier = set([start_node])
    while len(frontier) != 0:
        current_node = frontier.pop()
        neighbors = graph[current_node]
        for neighbor in neighbors:
            if neighbor not in result:
                frontier.add(neighbor)
                result.add(neighbor)
    return result


def test_reachable():
    graph = make_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B')])
    assert sorted(reachable(graph, 'A')) == ['A', 'B', 'C', 'D']

    graph = make_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B'), ('E', 'F'), ('F', 'G')])
    assert sorted(reachable(graph, 'A')) == ['A', 'B', 'C', 'D']
    assert sorted(reachable(graph, 'E')) == ['E', 'F', 'G']




def connected(graph):
    nodes = set(graph.keys())
    start_node = next(iter(nodes))
    reachable_nodes = reachable(graph, start_node)
    return nodes == reachable_nodes

def test_connected():
    graph = make_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B')])
    assert connected(graph) == True
    graph = make_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B'), ('E', 'F'), ('F', 'G')])
    assert connected(graph) == False



def n_components(graph):
    """
    Returns:
      the number of connected components in an undirected graph
    """
    nodes = set(graph.keys())
    num_components = 0

    while nodes:
        start_node = next(iter(nodes))
        reachable_nodes = reachable(graph, start_node)
        num_components += 1
        nodes = nodes - reachable_nodes

    return num_components


def test_n_components():
    assert n_components(make_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B')])) == 1
    assert n_components(make_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B'), ('E', 'F'), ('F', 'G')])) == 2
