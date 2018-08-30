class Graph:
    def __init__(self):
        self.vertices = set()
        self.edges = {}
        self.weights = {}

    def add_vertex(self, vertex):
        self.vertices.add(vertex)

    def add_edge(self, start_vertex, end_vertex, weight):
        if start_vertex in verticies and end_vertex in verticies:
            self.edges[start_vertex].append(end_vertex)
            self.edges[end_vertex].append(start_vertex)
            self.weights[(start_vertex, end_vertex)] = weight


def traverse_rec(graph, current, visited):
    if current not in visited:
        visited.add(current)
        print(current)
        for neighbor in graph.edges[current]:
            traverse_rec(graph, neighbor, visited)


def traverse(graph, current):
    visited = set()
    return traverse_rec(graph, current, visited)


verticies = {'a', 'b', 'c', 'd'}
edges = {}
edges['a'] = ['c']
edges['b'] = ['c','d']
edges['c'] = ['a','b','d']
edges['d'] = ['b','c']
graph = Graph()
graph.add_vertex('a')
graph.add_vertex('b')
graph.add_vertex('c')
graph.add_vertex('d')

graph.add_edge('a', 'c', 2)
graph.add_edge('c', 'b', 1)
graph.add_edge('c', 'd', 5)
graph.add_edge('b', 'd', 2)

traverse(graph, 'a')
