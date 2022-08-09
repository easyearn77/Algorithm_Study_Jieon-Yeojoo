import sys

n = int(sys.stdin.readline().rstrip())
stack = []

def push(x):
      stack.append(x)

def pop():
  if(not stack):
    return -1
  else:
    return stack.pop()

def size():
  return len(stack)

def empty():
  return 0 if stack else 1

def top():
  return stack[-1] if stack else -1


for _ in range(n):
  order = sys.stdin.readline().rstrip().split()

  input = order[0]

  if input == "push":
    push(order[1])
  elif input == "pop":
    print(pop())
  elif input == "size":
    print(size())
  elif input == "empty":
    print(empty())
  elif input == "top":
    print(top())
