import queue
import sys

class Graph:
    def __init__(self, nVertices):
        self.nVertices = nVertices
        self.adjMatrix = [[0 for i in range(nVertices)] for j in range(nVertices)]

    def addEdge(self, v1, v2, wt):
        self.adjMatrix[v1][v2] = wt
        self.adjMatrix[v2][v1] = wt

    def containsEdge(self, v1, v2):
        if self.adjMatrix[v1][v2] > 0:
            return True
        return False

    def removeEdge(self, v1, v2):
        if self.containsEdge(v1, v2) is False:
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0

    def __bfsHelper__(self, sv, visited):
        q = queue.Queue()
        q.put(sv)
        visited[sv] = True
        while not q.empty():
            currVertex = q.get()
            print(currVertex, end=" ")
            for i in range(self.nVertices):
                if self.adjMatrix[currVertex][i] > 0 and visited[i] is False:
                    q.put(i)
                    visited[i] = True

    def bfs(self):
        visited = [False for i in range(self.nVertices)]
        for i in range(self.nVertices):
            if visited[i] is False:
                self.__bfsHelper__(i, visited)
        
    def __dfsHelper__(self, sv, visited):
        print(sv, end=" ")
        visited[sv] = True
        for i in range(self.nVertices):
            if self.adjMatrix[sv][i] > 0 and visited[i] is False:
                self.__dfsHelper__(i, visited)

    def dfs(self):
        visited = [False for i in range(self.nVertices)]
        for i in range(self.nVertices):
            if visited[i] is False:
                self.__dfsHelper__(i, visited)

    def __str__(self):
        return str(self.adjMatrix)

    def __getMinVertex(self, visited, weight):
        minVertex = -1
        for i in range(self.nVertices):
            if (visited[i] is False and (minVertex == -1 or weight[i] < weight[minVertex])):
                minVertex = i
        return minVertex

    def prims(self):
        visited = [False for i in range(self.nVertices)]
        parent = [-1 for i in range(self.nVertices)]
        weight = [sys.maxsize for i in range(self.nVertices)]
        weight[0] = 0

        for i in range(self.nVertices-1):
            minVertex = self.__getMinVertex(visited, weight)
            visited[minVertex] = True

            # explore the neighbours of minVertex which is not visited 
            # and update the weight corresponding to that if required
            for j in range(self.nVertices):
                if self.adjMatrix[minVertex][j] > 0 and visited[j] is False:
                    if weight[j] > self.adjMatrix[minVertex][j]:
                        weight[j] = self.adjMatrix[minVertex][j]
                        parent[j] = minVertex
        
        for i in range(1, self.nVertices):
            if i < parent[i]:
                print(f"{i} {parent[i]} {weight[i]}")
            else:
                print(f"{parent[i]} {i} {weight[i]}")


li = [int(ele) for ele in input().split()]
n, E = li[0], li[1]
g = Graph(n)
for i in range(E):
    currInput = [int(ele) for ele in input().split()]
    g.addEdge(currInput[0], currInput[1], currInput[2])
    
g.prims()