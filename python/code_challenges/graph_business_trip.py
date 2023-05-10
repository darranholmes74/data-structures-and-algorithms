from data_structures.graph import Graph


def direct_flights(graph, cities):
    cost = 0

    for i in range(len(cities) - 1):
        node1 = None
        for node in graph.get_nodes():
            if node.value == cities[i]:
                node1 = node
                break
        node2 = None
        for node in graph.get_nodes():
            if node.value == cities[i+1]:
                node2 = node
                break
        if not node1 or not node2:
            return None
        neighbors = graph.adjacency_list[node1]
        for neighbor, weight in neighbors:
            if neighbor == node2:
                cost += weight
                break
        else:
            return None

    return True, cost



