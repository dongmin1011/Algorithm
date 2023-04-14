from collections import deque

def dfsfunc(start):
    
    
    # if visited[started-1] == False:
    #     visited[started-1] = True
    #     # print(started)
    #     print(started, end=' ')
        
    #     for i in range(len(graph)):
    #         if started == graph[i][0]:
    #             dfs(graph, visited, graph[i][1])
    #         elif started == graph[i][1]:
    #             dfs(graph, visited, graph[i][0])
             
    # else: return 
    visited[start] = True
    dfs.append(start)
    for i in node[start]:
        if visited[i]==False:
            dfsfunc(i)
        
    
def bfsfunc(start):
    q = deque()
    visited[start] =True
    bfs.append(start)
    
    q.append(start)
    
    
        
    while q:
        for i in node[q.popleft()]:
            if(visited[i] == False):
                visited[i] = True
                q.append(i)
                bfs.append(i)
        
        
        
    
    
    

N,M, start= map(int, input().split())

node =[[]for _ in range(N+1)]


for i in range(M):
    a, b = map(int, input().split())
    node[a].append(b)
    node[b].append(a)

# print(graph)
# print(a,b,start)
visited = [False]*(N+1)
# print(visited)
for i in range(N+1):
    # visited.append(False)
    node[i].sort()

# print(node)
# 
dfs = []
bfs = []

dfsfunc(start)
for i in dfs:
    print(i, end=' ')


for i in range(N+1):
    visited[i] = False
bfsfunc(start)
print()
for i in bfs:
    print(i, end=' ')




    