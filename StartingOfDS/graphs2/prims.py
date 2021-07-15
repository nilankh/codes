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

    def __str__(self):
        return str(self.adjMatrix)

    def __dfsHelper(self, sv, visited):
        print(sv)
        visited[sv] = True
        for i in range(self.nVertices):
            if(self.adjMatrix[sv][i] > 0 and visited[i] is False):
                self.__dfsHelper(i, visited)

    def dfs(self):
        visited = [False for i in range(self.nVertices)]
        self.__dfsHelper(0, visited)

    def __get_minVertex(self, visited, weight):

        min_vertex = -1
        for i in range(self.nVertices):
            #print("get ith", i)
            #print("wefjh",weight[min_vertex])
            if(visited[i] is False and (min_vertex == -1 or (weight[min_vertex] > weight[i]))):
                #print("wt of i", i)
                min_vertex = i
                #print("private function", min_vertex)
        return min_vertex
    def prims(self):
        visited = [False for i in range(self.nVertices)]
        parent = [-1 for i in range(self.nVertices)]
        weight = [sys.maxsize for i in range(self.nVertices)]
        weight[0] = 0
        for i in range(self.nVertices - 1):
            #print('outer for ith value', i)
            min_vertex = self.__get_minVertex(visited, weight)
            #print(min_vertex)
            visited[min_vertex] = True

            #explore the neighbours of minVertex which is not visited
            #and upadate the weight corresponding to them if required.
            for j in range(self.nVertices):
                #print("inner  j", j)
                if self.adjMatrix[min_vertex][j] > 0 and visited[j] is False:
                    #print("jth ", j)
                    if(weight[j] > self.adjMatrix[min_vertex][j]):
                        weight[j] = self.adjMatrix[min_vertex][j]
                        #print("wt of ",j, weight[j])
                        parent[j] = min_vertex
                        #print("parent of ",j,parent[j])
        for i in range(1, self.nVertices):
            if i < parent[i]:
                print(str(i) + " " + str(parent[i]) + " " + str(weight[i]))
            else:
                print(str(parent[i]) + " " + str(i) + " " + str(weight[i]))        
            
        
li = [int(ele) for ele in input().split()]
n = li[0]
E = li[1]

g = Graph(n)

for i in range(E):
    curr_input = [int(ele) for ele in input().split()]
    g.addEdge(curr_input[0], curr_input[1], curr_input[2])
    
g.prims()
    












        
