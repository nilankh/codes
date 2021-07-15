class Graph:
    def __init__(self, nVertices):
        self.nVertices = nVertices
        self.adjMatrix = [[0 for i in range(nVertices + 1)]for j in range(nVertices + 1)]

    def addEdge(self, v1, v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1

    def __str__(self):
        return str(self.adjMatrix)

    def __dfsH(self, sv, visited):
        print(sv)
        visited[sv]= True
        for i in range(self.nVertives):
            if self.adjMatrix[sv][i] > 0 and visited[i] is False:
                self.__dfsH(i, visited)
    def dfs(self):
        visited = [False for i in range(self.nVertices)]
        self.__dfsH(0, visited)
                          
##n = int(input()
g = Graph(3)
for i in range(1,3 + 1):
    g.addEdge(1,  i)
print(g)
