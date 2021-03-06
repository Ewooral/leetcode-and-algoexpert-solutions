#   Created by Elijah Boahen Owusu Ewooral
#   Copyright © 2022  optimize Code. All rights reserved.

from collections import defaultdict


class Graph:
    def __init__(self, numberofVertices):
        self.graph = defaultdict(list)
        self.numberofVertices = numberofVertices

    def addEdge(self, vertex, edge):
        self.graph[vertex].append(edge)

    def topogologicalSortUtil(self, v, visited, stack):
        visited.append(v)

        # Check if starting vertex has adjacent
        for i in self.graph[v]:
            if i not in visited:
                self.topogologicalSortUtil(i, visited, stack)

        stack.insert(0, v)

    def topologicalSort(self):

        visited = []
        stack = []

        for k in list(self.graph):
            if k not in visited:
                self.topogologicalSortUtil(k, visited, stack)

        print(stack)


customGraph = Graph(3)
customGraph.addEdge("A", "C")
customGraph.addEdge("C", "E")
customGraph.addEdge("E", "H")
customGraph.addEdge("E", "F")
customGraph.addEdge("F", "G")
customGraph.addEdge("B", "D")
customGraph.addEdge("B", "C")
customGraph.addEdge("D", "F")

customGraph.topologicalSort()
