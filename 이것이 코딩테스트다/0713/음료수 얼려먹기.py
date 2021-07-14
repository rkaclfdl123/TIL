n,m=map(int,input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int,input())))
result=0

def dfs(x,y):
    #y>=m 이 것때문에 오류 났음 0,0 부터 0,4 까지 돌아야하는데 n n 으로 놨다가 0,3 까지만 돔
    if x<=-1 or y<=-1 or x>=n or y>=m:
        return False
    if(graph[x][y]==0):
        graph[x][y]=1
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    return False

for i in range(n):
    for j in range(m):
        if(dfs(i,j)==True):
            result+=1

print(result)