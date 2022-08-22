import sys
input= sys.stdin.readline

dic= {}
for i in range(int(input())):
    dic[i+1]=set()

for j in range(int(input())):
    s,e=map(int,input().split())
    dic[s].add(e)
    dic[e].add(s)

visited=[]
def dfs(start,dic):
    for i in dic[start]:
        if i not in visited:
            visited.append(i)
            dfs(i,dic)

dfs(1,dic)
print(len(visited)-1)