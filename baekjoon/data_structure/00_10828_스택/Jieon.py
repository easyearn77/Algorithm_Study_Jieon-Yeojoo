import sys
class Stack:
    stack=[]
    def push(self,X):
        X=int(X)
        self.stack.append(X)
    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            return -1
    def size(self):
        return len(self.stack)
    def empty(self):
        if self.stack:
            return 0
        else:
            return 1
    def top(self):
        if self.stack:
            return self.stack[-1]
        else:
            return -1
p_stack=Stack()
n=int(input())
for _ in range(n):
    order=sys.stdin.readline().split()
    op=order[0]
    if op=='push':
        p_stack.push(order[1])
    elif op=='pop':
        print(p_stack.pop())
    elif op=='size':
        print(p_stack.size())
    elif op=='empty':
        print(p_stack.empty())
    elif op=='top':
        print(p_stack.top())

