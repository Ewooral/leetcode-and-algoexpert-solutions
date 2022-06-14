# two sum 
'''
array = [2, 5, 1, -1, 4, 3, 0]
target = 3

a + b = target
a = currentValue
b = nextValue

hash_t = {
    3 - 2=1: "Added",
    3 - 5=-2: "Added",
    3 - 1=2: "Added",
    3 -(-1)=4: "Added",
    3 - 4=-1: "not added",
    
    .
    .
    3 - 0: "Added",

}

'''


def two_sum(clist: list, target: int) -> list:
    hash_table = {}
    for value in clist:
        nextValue = target - value
        if nextValue in hash_table:
            print([value, nextValue])
        else:
            hash_table[value] = "Added"
    print(hash_table)
    return []




'''
[1, 3, 9, 1, 0]
'''
from collections import deque, defaultdict
from typing import List

from pandas import array
# from typing import Any

Queues = deque()
Queues.append(2)
Queues.append(20)
Queues.append(22)



class Graph:
    def __init__(self, graph: dict = None) -> None:
        if graph is None:
            graph = {}
        self.graph = graph

    def add_edge(self, vertex, edges) -> None:
        self.graph[vertex].append(edges)

def hasSingleCycle(customList: List) -> bool:
    numOfElementsVisited:int = len(customList)
    currentIndex:int = 0
    while numOfElementsVisited < len(customList):
        if numOfElementsVisited > 0 and currentIndex == 0:
            return False
        numOfElementsVisited += 1
        currentIndex = getNextIndex(currentIndex, customList)
    return currentIndex == 0

def getNextIndex(currentIndex, customList):
    jump = customList[currentIndex]
    nextIndex = (currentIndex + jump) % len(customList)
    if nextIndex >=0:
        return nextIndex
    else:
        nextIndex + len(customList)





def main() -> None:
    # queue
    print(Queues)
    Queues.popleft()
    print(Queues)

    # two sum problem
    print("............")
    two_sum([2, 5, 1, -1, 4, 3, 0], 3)

    print("............")
    # graph
    graph = Graph({})
    graph.graph.update({"Kumasi": ["dropong", "Frante", "T_Krom"]})
    graph.add_edge("Kumasi", "d")
    print(graph.graph)
    print(hasSingleCycle(customList=[2, 1, -1]))

if __name__ == "__main__":
    main()

