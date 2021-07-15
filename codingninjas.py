

def codingninjas(arr):
    c = "CODINGNINJA"
    for i in range(0, len(arr)):
        for j in range(0, len(arr)):
            if(arr[i][j] == 'C'):
                visited = [[False for i in range(row)]for j in range(col)]
                if(dfs(arr, i, j,     


row,col=map(int,input().split())
arr=[[0 for x in range(col)] for x in range(row)]

for b in range(row):
    string=input()
    
    for c in range(len(string)):
        arr[b][c]=string[c]
codingninjas(arr)
print(arr)
