import math
import sys

input=sys.stdin.readline

n=int(input())
numbers=list(map(int,input().split()))
gcd_=math.gcd(math.gcd(numbers[0],numbers[1]),numbers[-1])
result=[]

for i in range(1,int(math.sqrt(gcd_))+1):
    if gcd_%i==0:
        result.append(i)
        if i**2!=gcd_: result.append(gcd_//i)

result.sort()
for num in result:
    print(num)