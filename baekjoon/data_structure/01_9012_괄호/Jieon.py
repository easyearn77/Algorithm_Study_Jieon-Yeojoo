import sys
t=int(sys.stdin.readline())
for _ in range(t):
    ps=sys.stdin.readline()
    n=0
    flag=True
    for p in ps:
        if p=='(':
            n+=1
        elif p==')':
            n-=1
            if n<0:
                flag=False
                break
    if n!=0:
        flag=False
    
    if flag:
        print("YES")
    else:
        print("NO")    