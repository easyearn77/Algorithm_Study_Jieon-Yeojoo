from collections import deque
import sys

n = int(sys.stdin.readline())
q = deque([i + 1 for i in range(n)])

while len(q) > 1:
    q.popleft()
    temp = q.popleft()
    q.append(temp)

print(q[0])