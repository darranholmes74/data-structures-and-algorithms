class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_node(self, value):
        node = Vertex(value)
        self.adjacency_list[node] = []
        return node

    def add_edge(self, start_vertex, end_vertex, weight=0):
        if start_vertex not in self.adjacency_list:
            raise KeyError('The starting vertex in not in the graph')
        if end_vertex not in self.adjacency_list:
            raise KeyError('The end vertex is not in graph')
        self.adjacency_list[start_vertex].append((end_vertex, weight))
        self.adjacency_list[end_vertex].append((start_vertex, weight))

    def get_neighbors(self, vertex):
        return [edge[0] for edge in self.adjacency_list[vertex]]

    def get_nodes(self):
        return self.adjacency_list.keys()

    def size(self):
        return len(self.adjacency_list)


class Vertex:
    def __init__(self, value):
        self.value = value
