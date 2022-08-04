from collections import deque
import sys

n=int(sys.stdin.readline())

graph=[[] for _ in range(n+1)]
parent=[0 for _ in range(n+1)]

for i in range(n-1):
    s,e=map(int, sys.stdin.readline().split())
    graph[s].append(e)
    graph[e].append(s)

def bfs():
    q=deque()
    q.append(1) 
    while(q):
        node= q.popleft()
        for i in graph[node]:
            if parent[i]==0:
                parent[i]=node
                q.append(i)
    return parent

bfs()

for i in parent[2:]:
    print(i)