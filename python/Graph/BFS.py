class Graph:
    def __init__(self, graphDic = None):
        if graphDic is None:
            graphDic = {}
        self.graphDic = graphDic

    def addGraph(self, vertex, edge):
        self.graphDic[vertex].append(edge)
        
     # O(v + e) T, O(v) S
    def BFS(self, vertex):
        visited = [vertex]
        queue = [vertex]
        while len(queue) > 0:
            deVertex = queue.pop(0) # prints the first element
            print(deVertex)
            for adjacentVertex in self.graphDic[deVertex]:
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
print(graph.graphDic)
print("...insert...")
# let's add edge f to the graph 
graph.addGraph("e", "f")
print(graph.graphDic)
print("...traverse(BFS)...")
graph.BFS("a")
print()
graph2 = Graph(anotherDic)
graph2.BFS("a")