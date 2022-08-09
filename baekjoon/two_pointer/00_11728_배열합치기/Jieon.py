import sys

input= sys.stdin.readline

na,nb=map(int,input().split())
list_a= list(map(int,input().split()))
list_b= list(map(int,input().split()))

point_a=0
point_b=0
result=[]
while (point_a<na and point_b<nb):
    if list_a[point_a]<list_b[point_b]:
        result.append(list_a[point_a])
        point_a+=1
    else:
        result.append(list_b[point_b])
        point_b+=1

if point_a<na:
    result.extend(list_a[point_a:])
else:
    result.extend(list_b[point_b:])

print(*result)
