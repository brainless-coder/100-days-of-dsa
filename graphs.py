import queue


class Graph:
    def __init__(self, nVertices):
        self.nVertices = nVertices
        self.adjMatrix = [[0 for i in range(nVertices)] for j in range(nVertices)]

    def addEdge(self, v1, v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1

    def removeEdge(self, v1, v2):
        if self.containsEdge(v1, v2) is False:
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0

    def containsEdge(self, v1, v2):
        if self.adjMatrix[v1][v2] > 0:
            return True
        return False

    def __dfsHelper(self, sv, visited):
        print(sv)
        visited[sv] = True
        for i in range(self.nVertices):
            if self.adjMatrix[sv][i] > 0 and visited[i] is False:
                self.__dfsHelper(i, visited)

    def dfs(self):
        visited = [False for i in range(self.nVertices)]
        for i in range(self.nVertices):
            if visited[i] is False:
                self.__dfsHelper(i, visited)

    def __bfsHelper(self, sv, visited):
        q = queue.Queue()
        q.put(sv)
        visited[sv] = True
        while not q.empty():
            curr_vertex = q.get()
            print(curr_vertex)
            for i in range(self.nVertices):
                if self.adjMatrix[curr_vertex][i] > 0 and visited[i] is False:
                    q.put(i)
                    visited[i] = True

    def bfs(self):
        visited = [False for i in range(self.nVertices)]
        for i in range(self.nVertices):
            if visited[i] is False:
                self.__bfsHelper(i, visited)

    def __hasPathHelper(self, v1, v2, visited):
        if self.adjMatrix[v1][v2] > 0:
            return True
        
        visited[v1] = True
        for i in range(self.nVertices):
            if self.adjMatrix[v1][i] > 0 and visited[i] is False:
                if self.__hasPathHelper(i, v2, visited):
                    return True
        return False

    def hasPath(self, v1, v2):
        visited = [False] * self.nVertices
        return self.__hasPathHelper(v1, v2, visited)

    def __getPathDFSHelper(self, v1, v2, visited):
        if self.adjMatrix[v1][v2] > 0:
            return [v2, v1]
        
        visited[v1] = True
        for i in range(self.nVertices):
            if self.adjMatrix[v1][i] > 0 and visited[i] is False:
                if self.__getPathDFSHelper(i, v2, visited) is not None:
                    ans = self.__getPathDFSHelper(i, v2, visited)
                    ans.append(v1)
                    return ans
        # return None
        
    def getPathDFS(self, v1, v2):
        visited = [False] * self.nVertices
        return self.__getPathDFSHelper(v1, v2, visited)

    # if we direclty call the class, then this objects gets printed
    def __str__(self):
        return str(self.adjMatrix)




g = Graph(7)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(0, 3)
g.addEdge(1, 5)
g.addEdge(2, 4)
g.addEdge(4, 6)
g.addEdge(3, 6)
# print(g)
# g.dfs()
# g.bfs()
# print(g.hasPath(5, 0))
print(g.getPathDFS(0, 6))