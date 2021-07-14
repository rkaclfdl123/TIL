from collections import deque

def bfs(graph,i,visited):
    queue=deque([i])
    visited[i]=True 
    while(queue):
        v=queue.popleft()
        print(v)
        for i in graph[v]:
            if(visited[i]==False):
                queue.append(i)



graph=[
    [],      #0
    [2,3,8], #1
    [1,7],   #2
    [1,4,5], #3
    [3,5],   #4
    [3,4],   #5
    [7,8],   #6
    [2,6,8], #7
    [1,7]    #8
]

visited=[False]*9
bfs(graph,1,visited)