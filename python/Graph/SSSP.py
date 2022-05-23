# Single Source Shorest Path

class Graph:
    def __init__(self, graphDic=None):
        if graphDic is None:
            graphDic = {}
        self.graphDic = graphDic

    
    def BFS(self, start, end):
        queue = []
        queue.append([start])
        while queue:
            path = queue.pop(0)
            node = path[-1]
            if node == end:
                return path
            for adjancent in self.graphDic.get(node, []):
                new_path = list(path)
                new_path.append(adjancent)
                queue.append(new_path)


customDict = {"a": ["b", "c"],
              "b": ["d", "g"],
              "c": ["d", "e"],
              "d": ["f"],
              "e": ["f"],
              "g": ["f"]
              }

graph = Graph(customDict)
print(graph.BFS("a", "f"))
print(graph.BFS("a", "e"))
