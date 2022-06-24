# Create A Graph data structure
from collections import defaultdict
from dataclasses import dataclass


@dataclass
class Graph:
    graph: dict = None
    if graph is None:
        graph = defaultdict
    else:
        graph = None

    def addVertex(self, vertex, edge):
        self.graph[vertex].append(edge)


def find_path(graph, start, end, path=None):
    if path is None:
        path = []
    path = path + [start]
    if start == end:
        return path
    if graph.get(start) is None:
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath: return newpath
    return None


graph = Graph({})

graph.graph.update({"a": ["b", "c"],
                    "b": ["a", "d", "e"],
                    "c": ["a", "e"],
                    "d": ["b", "e", "f"],
                    "e": ["d", "c"],
                    "f": ["d", "e"]})

G = graph.graph
print(G)
print(find_path(G, 'b', 'a'))
