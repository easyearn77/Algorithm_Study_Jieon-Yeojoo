import sys
from collections import deque
class queue:
    q=deque([])
    def push(self,X):
        self.q.append(int(X))
    def pop(self):
        if self.q:
            return self.q.popleft()
        else:
            return -1
    def size(self):
        return len(self.q)
    def empty(self):
        if self.q:
            return 0
        else:
            return 1
    def front(self):
        if self.q:
            return self.q[0]
        else:
            return -1
    def back(self):
        if self.q:
            return self.q[-1]
        else:
            return -1

n=int(sys.stdin.readline())
test_q=queue()

for _ in range(n):
    order=sys.stdin.readline().split()
    operation=order[0]
    if operation=='push':
        test_q.push(order[1])
    elif operation=='pop':
        print(test_q.pop())
    elif operation=='size':
        print(test_q.size())
    elif operation=='empty':
        print(test_q.empty())
    elif operation=='front':
        print(test_q.front())
    elif operation=='back':
        print(test_q.back())

