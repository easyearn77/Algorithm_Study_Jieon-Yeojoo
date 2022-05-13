from collections import deque
import sys

n=int(sys.stdin.readline())
queue=deque([i+1 for i in range(n)])

while len(queue)>1:
    queue.popleft()
    temp=queue.popleft()
    queue.append(temp)

print(queue[0])