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
                ans = self.__getPathDFSHelper(i, v2, visited)
                if ans:
                    ans.append(v1)
                    return ans

    def getPathDFS(self, v1, v2):
        visited = [False for i in range(self.nVertices)]
        return self.__getPathDFSHelper(v1, v2, visited)

    def getPathBFS(self, v1, v2):
        visited = [False] * self.nVertices
        q = queue.Queue()
        q.put(v1)
        visited[v1] = True
        parent = {}
        while not q.empty():
            front = q.get()
            for i in range(self.nVertices):
                if self.adjMatrix[front][i] > 0 and visited[i] == False:
                    q.put(i)
                    visited[i] = True
                    parent[i] = front
                    if i == v2:
                        break
        path = [v2]
        i = v2
        while i != v1:
            if parent.get(i) is not None:
                path.append(parent[i])
                i = parent[i]
            else:
                return None
        return path
        
    def __isConnectedHelper(self, sv, visited):
        visited[sv] = True
        for i in range(self.nVertices):
            if self.adjMatrix[sv][i] > 0 and visited[i] is False:
                self.__isConnectedHelper(i, visited)

    def isConnected(self):
        visited = [False] * self.nVertices
        self.__isConnectedHelper(0, visited)
        for ele in visited:
            if ele == False:
                return False
        return True

    def __connectedComponentsHelper(self, sv, visited, list):
        visited[sv] = True
        list.append(sv)
        for i in range(self.nVertices):
            if self.adjMatrix[sv][i] > 0 and visited[i] is False:
                self.__connectedComponentsHelper(i, visited, list)
        return list

    def connectedComponents(self):
        visited = [False for i in range(self.nVertices)]
        output = []
        for i in range(self.nVertices):
            if visited[i] is False:
                comp = self.__connectedComponentsHelper(i, visited, [])
                output.append(comp)
        return output

    # if we direclty call the class, then this objects gets printed
    def __str__(self):
        return str(self.adjMatrix)




g = Graph(8)
g.addEdge(0, 7)
g.addEdge(3, 5)
g.addEdge(3, 6)
g.addEdge(1, 2)
g.addEdge(1, 4)
# print(g)
# g.dfs()
# g.bfs()
# print(g.hasPath(5, 0))
# print(g.getPathDFS(5, 6))
# print(g.isConnected())
print(g.connectedComponents())
