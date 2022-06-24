from dataclasses import dataclass
from collections import defaultdict


@dataclass
class Graph:
    graph: dict = None
    if graph is None:
        graph = defaultdict
    else:
        graph = None

    def addVertex(self, vertex, edge):
        self.graph[vertex].append(edge)

    # O(v + e) T, O(v) S
    def BFS(self, vertex, value):
        visited = [vertex]
        queue = [vertex]
        while len(queue) > 0:
            deVertex = queue.pop(0)  # prints the first element
            print(deVertex)
            if deVertex == value:
                adjacent_neighbors = self.graph[deVertex]
                return adjacent_neighbors
            for adjacentVertex in self.graph[deVertex]:
                if adjacentVertex not in visited:
                    visited.append(adjacentVertex)
                    queue.append(adjacentVertex)


customDic = {
    "a": ["b", "c"],
    "b": ["a", "d", "e"],
    "c": ["a", "e"],
    "d": ["b", "e", "f"],
    "e": ["d", "c"],
    "f": ["d", "e"],
}
anotherDic = {
    "a": ["b", "c", "d"],
    "b": ["e", "f"],
    "c": [],
    "d": ["g", "h"],
    "e": [],
    "f": ["i", "j"],
    "g": ["k"],
    "h": [],
    "i": [],
    "j": [],
    "k": []

}
graph = Graph(customDic)
print(graph.graph)
print("...insert...")

# let's add edge f to the graph
graph.addVertex("e", "f")
graph.addVertex("e", "b")
print(graph.graph)
print("...traverse(BFS)...")
print("Adjacent neighbors: ", graph.BFS("a", "f"))
print()
graph2 = Graph(anotherDic)
# graph2.BFS("f")

# update the Graph
graph.graph.update({"Bloomberg": ["Elijah", 29, "$230,000/yr"]})
print(graph.graph)
graph.addVertex("Bloomberg", "Tema")
print(graph.graph)