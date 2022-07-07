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


def find_path(graph, start, end, path=None):
    # print("find_path", "(", path, ")")
    if path is None:
        path = []
    path += [start]
    if start == end:
        return path
    for node in graph[start]:
        if node not in path:
            new_path = find_path(graph, node, end, path)
            if len(new_path) > 0:
                return new_path
        # return "Cycle has been detected!"
    return None


customDict = {"a": ["b", "c"],
              "b": ["d", "g"],
              "c": ["d", "e"],
              "d": ["f"],
              "e": ["f"],
              "g": ["f"]
              }
ano = {
    "a": ["b", "c"],
    "b": ["a", "d", "e"],
    "c": ["a", "e"],
    "d": ["b", "e", "f"],
    "e": ["d", "c"],
    "f": ["d", "e"]
}

graph = Graph(customDict)
graph1 = Graph(ano)

print(graph1.BFS("a", "f"))
print(graph1.BFS("a", "e"))
# print(find_path(graph.graphDic, "a", "e"))
# print(find_path(graph.graphDic, "a", "f"))