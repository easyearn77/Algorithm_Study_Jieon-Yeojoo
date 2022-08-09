n = int(input())
num = list(map(int, input().split()))
answer = []

for i in range(1, min(num) + 1):
    if n == 2:
        if num[0] % i == 0 and num[1] % i == 0:
            answer.append(i)
    else:
        if num[0] % i == 0 and num[1] % i == 0 and num[2] % i == 0:
            answer.append(i)

for i in answer:
    print(i)