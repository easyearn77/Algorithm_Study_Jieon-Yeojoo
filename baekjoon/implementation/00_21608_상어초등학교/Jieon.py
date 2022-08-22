import sys

input= sys.stdin.readline

dx=[0,-1,0,1]
dy=[-1,0,1,0]

n=int(input());
arr= [[0]*n for _ in range(n)]
students= [list(map(int,input().split())) for _  in range(n**2)]

for order in range(n**2):
    student = students[order]
    tmp= [] #가능한 자리
    for i in range(n):
        for j in range(n):
            if arr[i][j]==0:
                like=0
                blank=0
                for k in range(4):
                    nx, ny= i+dx[k], j+dy[k]
                    if 0<=nx<n and 0<=ny<n:
                        if arr[nx][ny] in student[1:]:
                            like+=1
                        if arr[nx][ny] == 0 : 
                            blank+=1
                tmp.append([like,blank,i,j])
    tmp.sort(key=lambda x: (-x[0],-x[1],x[2],x[3]))
    arr[tmp[0][2]][tmp[0][3]]=student[0]

result=0
students.sort()

for i in range(n):
    for j in range(n):
        ans=0
        for k in range(4):
            nx,ny=i+dx[k],j+dy[k]
            if 0<=nx<n and 0<=ny<n:
                if arr[nx][ny] in students[arr[i][j]-1]:
                    ans+=1
        if ans!=0:
            result+=10**(ans-1)

print(result)