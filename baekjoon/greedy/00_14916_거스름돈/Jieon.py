n= int(input())
n5= n//5
rest= n%5
result=0

while rest<=n:
    if rest==0: 
        result=n5
        break
    else:
        if rest%2==0:
            result=n5+rest//2
            break
        else:
            n5-=1
            rest+=5

if result==0 : print(-1)
else : print(result)
