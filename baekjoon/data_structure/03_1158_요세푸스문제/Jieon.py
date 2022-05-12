import sys
from collections import deque

n,k=map(int,sys.stdin.readline().split())
list=deque([i+1 for i in range(n)])
answer=[]
while list:
    list.rotate(-(k-1))
    answer.append(list.popleft())

answer_str='<'+str(answer)[1:-1]+'>'
print(answer_str)
