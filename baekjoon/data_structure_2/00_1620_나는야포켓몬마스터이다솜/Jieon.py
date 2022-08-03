from curses.ascii import isalpha, isdigit
import sys
input=sys.stdin.readline

pocketmon={}
pocketmon_list=['_']
                                                                                                                                                                                                                  
n,m=map(int,input().split())
for i in range(1,n+1):
    v=input().rstrip()
    pocketmon[v]=i
    pocketmon_list.append(v)
for _ in range(m):
    value=input().rstrip()
    if value.isalpha():
        print(pocketmon.get(value))
    elif value.isdigit():
        print(pocketmon_list[int(value)])
