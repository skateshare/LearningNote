"""
Graph:
BFS : pros : shortest path(unweited) , closer Nodes,  cons : more memory

DFS : pros : less memory , does path exist , cons: can get slow

note the way to construct a graph:
- adjacent matrix
- adjacent list
- edge list
"""

class Graph():
    def __init__(self):
        self.noOfNodes = 0
        self.adjacentList = dict()

    def addVertex(self, node):
        if self.adjacentList.get(node) != None:
            print("the node:" + node + "already exist")
        else:
            self.adjacentList[node] = []
            self.noOfNodes += 1

    def addEdge(self, node1, node2):
        if self.adjacentList.get(node1) == None or self.adjacentList.get(node2) == None:
            print("nodes are not exist")
        else:
            if node2 not in self.adjacentList[node1]:
                self.adjacentList[node1].append(node2)
            if node1 not in self.adjacentList[node2]:
                self.adjacentList[node2].append(node1)

    def showConnections(self):
        for k, v in self.adjacentList.items():
            print(k + "--->" , end=" ")
            for i in v:
                print(i + " ", end = " ")
            print(" ")
