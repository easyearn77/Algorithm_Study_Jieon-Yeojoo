import sys


class Stack:
    stack=[]
    def push(self,x):
        self.stack.append(x)
    def pop(self):
        if self.stack: return self.stack.pop()
        else: return -1
    def size(self):
        return len(self.stack)
    def empty(self):
        if self.stack: return 0
        else: return 1
    def top(self):
        if self.stack: return self.stack[-1]
        else: return -1

stack= Stack()
n=int(input())
for i in range(n):
    inst=sys.stdin.readline().split()
    op=inst[0]
    if op=='push':
        stack.push(int(inst[1]))
    elif op=='pop':
        print(stack.pop())
    elif op=='size':
        print(stack.size())
    elif op=='empty':
        print(stack.empty())
    elif op=='top':
        print(stack.top())
    