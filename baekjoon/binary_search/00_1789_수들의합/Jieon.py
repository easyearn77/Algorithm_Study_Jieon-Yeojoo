n=int(input())
start= 1
end=n
ans=0
while start<=end:
    mid= (start+end)//2
    if (mid*(mid+1)/2 <=n):
        ans=mid
        start=mid+1
    else:
        end=mid-1

print(ans)