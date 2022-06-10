class Graph:
    def __init__(self, graphDic=None):
        if graphDic is None:
            graphDic = {}
        self.graphDic = graphDic

    def addGraph(self, vertex, edge):
        self.graphDic[vertex].append(edge)

    # O(v + e) T, O(v) S
    def DFS(self, vertex):
        visited = [vertex]
        stack = [vertex]
        while stack:
            popVertex = stack.pop()  # prints the last element
            print(popVertex)
            # Check for adjacent vertices and push them to the stack and set the current Vertices as visited
            for adjacentVertex in self.graphDic[popVertex]:
                if adjacentVertex not in visited:
                    visited.append(adjacentVertex)
                    stack.append(adjacentVertex)


customDic = {
    "a": ["b", "c"],
    "b": ["a", "d", "e"],
    "c": ["a", "e"],
    "d": ["b", "e", "f"],
    "e": ["d", "c"],
    "f": ["d", "e"],
}

graph = Graph(customDic)
print(graph.graphDic)
print("...insert...")
# let's add edge f to the graph
graph.addGraph("e", "f")
print(graph.graphDic)
print("...traverse(DFS)...")
graph.DFS("f")


class Node:
    def __init__(self, name) -> None:
        self.children = []
        self.name = name

    def __str__(self) -> str:
        return self.name
    
    def addChild(self, name):
        self.children.append(Node(name))

    def depthFirstSearch(self, array):
        array.append(self.name)
        for child in self.children:
            child.depthFirstSearch(array)
        return array

graph = Node("Acc")
graph.addChild("Kum")
graph.addChild("Kam")
graph.addChild("Kibi")
graph.addChild("Kumchacha")
print(graph.children[3])
print(graph.depthFirstSearch([0]))