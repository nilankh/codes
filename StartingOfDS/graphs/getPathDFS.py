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
        return True if self.adjMatrix[v1][v2] > 0 else False

    def __str__(self):
        return str(self.adjMatrix)
    
    def __getPathDFShelper(self, sv, ev, visited):
        if sv == ev:
            return list([sv])
        visited[sv] = True
        for i in range(self.nVertices):
            if self.adjMatrix[sv][i] > 0 and visited[i] is False:
                li = self.__getPathDFShelper(i, ev, visited)
                if li != None:
                    li.append(sv)
                    return li
        return None
    def getPathDFS(self, sv, ev):
        visited = [False for i in range(self.nVertices)]
        for i in range(self.nVertices):
            if visited[i] is False:
                return self.__getPathDFShelper(sv, ev, visited)

    

li = [int(x) for x in input().split()]
v = li[0]
e = li[1]
g = Graph(v)
for i in range(e):
    a, b = [int(x) for x in input().split()]
    g.addEdge(a, b)
li1 = [int(x) for x in input().split()]
sv = li1[0]
ev = li1[1]

k = g.getPathDFS(sv, ev)
if k != None:
    for element in k:
        print(element, end = ' ')
        








