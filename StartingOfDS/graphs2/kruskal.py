class Edge:
    def __init__(self, src, dest, wt):
        self.src = src
        self.dest = dest
        self.wt = wt
def getParent(v, parent):
    if(v == parent[v]): #it is actual Parent
        return v
    return getParent(parent[v], parent)
        
def kruskal(edges, nVertices):
    parent = [i for i in range(nVertices)] #starting me for 0 it is 0 for 1 it is 1 for 2 it is 2
    #print(parent)
    edges = sorted(edges, key = lambda edge:edge.wt)#lambda function give access to object
    count = 0

    output = [] #in which we will put all the edges (n - 1) edegs in MST
    i = 0
    while(count < (nVertices - 1)):# we will keep appending edges in the MST till the count is less than n -1
        #we will append only if parent of v1 and v2 should be different
        currentEdge = edges[i]
        #print(currentEdge.src)
        #print(currentEdge.dest)
        #print(currentEdge.wt)
        srcParent = getParent(currentEdge.src, parent)
        destParent = getParent(currentEdge.dest, parent)

        if srcParent != destParent:
            output.append(currentEdge)
            count += 1
            parent[srcParent] = destParent
            #print(srcParent)
            #print(destParent)
        i += 1
    return output
    
li = [int(x) for x in input().split()]
n = li[0] #no of vertices
E = li[1] #no of edges
edges = []
for i in range(E):
    curr_input = [int(x) for x in input().split()]
    src = curr_input[0]
    dest = curr_input[1]
    wt = curr_input[2]
    edge = Edge(src, dest, wt)
    #print(str(edge.src))
    edges.append(edge)
output = kruskal(edges, n)
for edge in output:
    if edge.src < edge.dest:
        print(str(edge.src) + " " + str(edge.dest) + " " + str(edge.wt))
    else:
        print(str(edge.dest) + " " + str(edge.src) + " " + str(edge.wt))
        
        



