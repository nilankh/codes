class Graph:
    def __init__(self, nVertices):
        self.nVertices = nVertices
        self.adjMatrix = [[0 for i in range(nVertices + 1)] for j in range(nVertices + 1)]

    def addEdge(self, v1, v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1

    def removeEdge(self):
        if self.containsEdge(v1, v2) is False:
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0

    def containsEdge(self, v1, v2):
        return True if self.adjMatrix[v1][v2] > 0 else False

    def __str__(self):
        return str(self.adjMatrix)
    
    def __islandHelper(self, visited,vertex):
        visited[vertex] = True
        
        for i in range(1,self.nVertices + 1):
            if self.adjMatrix[vertex][i] == 1 and visited[i] is False:
                self.__islandHelper(visited, i)
        
        

    def island(self):
        visited = [False for i in range(self.nVertices+1)]
        print(visited)
        count = 0
        for i in range(1,self.nVertices + 1):
            if visited[i] is False:

                self.__islandHelper(visited,i)
                count += 1
        return count

li = [int(x) for x in input().split()]
V = li[0]
E = li[1]
g = Graph(V)
li1 = [int(x) for x in input().split()]
li2 = [int(x) for x in input().split()]
i=0
for x in range(E):
    # arr = [int(x) for x in input().split()]
    v1 = li1[i]
    v2 = li2[i]
    i+=1
    g.addEdge(v1, v2)
print(g)
##li = [int(x) for x in input().split()]
##V = li[0]
##E = li[1]
##g = Graph(V)
##for i in range(E):
##    arr = [int(x) for x in input().split()]
##    v1 = arr[0]
##    v2 = arr[1]
##    g.addEdge(v1, v2)
##print(g)
ans = g.island()
print(ans)



















