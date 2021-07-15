import sys
class Graph:
    def __init__(self, nVertices):
        self.nVertices = nVertices
        self.adjMatrix = [[0 for i in range(nVertices)] for j in range(nVertices)]

    def addEdge(self, v1, v2, wt):

        self.adjMatrix[v1][v2] = wt
        self.adjMatrix[v2][v1] = wt

    def removeEdge(self, v1, v2):
        if self.containsEdge(v1, v2) is False:
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0

    def containsEdge(self, v1, v2):
        return True if self.adjMatrix[v1][v2] > 0 else False


    def __getMinVertex(self, visited, weight):
        minVertex = -1
        for i in range(self.nVertices):
            if(visited[i] is False and (minVertex == -1 or (weight[minVertex] > weight[i]))):
                minVertex = i
        return minVertex
    def dijkstra(self):
        visited = [False for i in range(self.nVertices)]
        distance = [sys.maxsize for i in range(self.nVertices)]
        distance[0] = 0
        for i in range(self.nVertices - 1):
            minVertex = self.__getMinVertex(visited, distance)
            visited[minVertex] = True
            
            #exploring all neighbours
            for j in range(self.nVertices):
                if(self.adjMatrix[minVertex][j] > 0 and visited[j] is False):
                    if(distance[j] > distance[minVertex] + self.adjMatrix[minVertex][j]):
                        distance[j] = distance[minVertex] + self.adjMatrix[minVertex][j]

        for i in range(self.nVertices):
            print(str(i) + " " + str(distance[i]))

    
li = [int(ele) for ele in input().split()]
n = li[0]
E = li[1]

g = Graph(n)

for i in range(E):
    curr_input = [int(ele) for ele in input().split()]
    g.addEdge(curr_input[0], curr_input[1], curr_input[2])
    
g.dijkstra()




                  
