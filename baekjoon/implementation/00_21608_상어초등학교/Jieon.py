import sys

input= sys.stdin.readline

dx=[0,-1,0,1]
dy=[-1,0,1,0]

n= int(input())
like_dic={}
map= [[0]*n for _ in range(n)]

for _ in range(n*n):
    likes= list(map(int,input().split()))
    like_dic[likes[0]]=likes[1:]
    num=likes[0]
    max_x=0
    max_y=0
    max_like =-1
    max_empty= -1

    for i in range(n):
        for j in range(n):
            like_cnt=0 
            empty_cnt=0
            if map[i][j]==0:
                like_cnt=0
                empty_cnt=0
                for k in range(4):
                    nx= i+dx[k]
                    ny= i+dy[k]
                    if 0<=nx<n and 0<=ny<n:
                        if map[nx][ny] in like_dic[num]:
                            like_cnt+=1
                        if map[nx][ny]:
                            empty_cnt+=1
                if max_like < like_cnt or (max_like==like_cnt and max_empty < empty_cnt):
                    max_x=i
                    max_y=j
                    max_like=like_cnt
                    max_empty=empty_cnt
    map[max_x][max_y]=num

answer=0
for i in range(n):
    for j in range(n):
        cnt=0
        for k in range(4):
            nx= i+dx[k]
            ny=i+dy[k]
            if 0<=nx<n and 0<=ny<n:
                if map[nx][ny] in like_dic[map[i][j]]:
                    cnt+=1
        if cnt!=0:
            answer+=10**(cnt-1)

print(answer)
