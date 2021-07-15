
class Graph:
    def __init__(self, nVertices):
        self.nVertices = nVertices
        self.adjMatrix = [[0 for i in range(nVertices)] for j in range(nVertices)]

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

    def __connectedComponentsHelper(self, visited, smallOutput, vertex):
        visited[vertex] = True
        smallOutput.append(vertex)
        for i in range(self.nVertices):
            if self.adjMatrix[vertex][i] == 1 and visited[i] is False:
                self.__connectedComponentsHelper(visited, smallOutput, i)

                
    def allConnectedComponents(self):
        visited = [False for i in range(self.nVertices)]
        output = []
        for i in range(self.nVertices):
            if visited[i] is False:
                smallOutput = list()
                self.__connectedComponentsHelper(visited, smallOutput, i)
                output.append(smallOutput)
                #print(output)
        return output


li = [int(x) for x in input().split()]
V = li[0]
E = li[1]

g = Graph(V)

for i in range(E):
    arr = [int(x) for x in input().split()]
    v1 = arr[0]
    v2 = arr[1]
    g.addEdge(v1, v2)

ans = g.allConnectedComponents()

if ans != None:
    for ele in ans:
        
        ele.sort()
        #print("ele", ele)
        for k in ele:
            print(k, end = " ")
        print()













    
