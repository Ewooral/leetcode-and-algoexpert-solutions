class Graph:
    def __init__(self, graphDic = None):
        if graphDic is None:
            graphDic = {}
        self.graphDic = graphDic

    def addGraph(self, vertex, edge):
        self.graphDic[vertex].append(edge)
    # O(V + E) S, T
    def BFS(self, vertex):
        visited = [vertex]
        queue = [vertex]
        while queue:
            deVertex = queue.pop(0) # prints the first element
            print(deVertex)
            for adjacentVertex in self.graphDic[deVertex]:
                if adjacentVertex not in visited:
                    visited.append(adjacentVertex)
                    queue.append(adjacentVertex)

    
    def DFS(self, vertex):
        visited = [vertex]
        stack = [vertex]
        while stack:
            popVertex = stack.pop() # prints the last element
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
print("...traverse(BFS)...")
graph.BFS("a")
print("...traverse(DFS)...")
graph.DFS("a")
