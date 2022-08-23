import sys
from collections import deque

input = sys.stdin.readline

n,l,r= map(int,input().split())
people= [list(map(int,input().split())) for _ in range(n)]

dx= [0,0,1,-1]
dy= [1,-1,0,0]

def bfs(sx,sy,index):
    queue= deque()
    queue.append((sx,sy))

    united=[]
    united.append((sx,sy))
    total= people[sx][sy]
    cnt=1
    union[sx][sy]=index
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n and union[nx][ny]==-1:
                if l<=abs(people[x][y]-people[nx][ny])<=r:
                    queue.append((nx,ny))
                    union[nx][ny]=index
                    united.append((nx,ny))
                    total+=people[nx][ny]
                    cnt+=1
    for i, j in united:
        people[i][j]=total//cnt
    return cnt

time=0
while True:
    union=[[-1]*n for _ in range(n)]
    index=0
    for i in range(n):
        for j in range(n):
            if union[i][j]==-1:
                bfs(i,j,index)
                index+=1
    if index==n*n: break
    time+=1

print(time)
