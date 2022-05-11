n = int(input())
for _ in range(n):
    arr = input()
    sum = 0
    for a in arr:
        if a == '(':
            sum += 1
        elif a == ')':
            sum -= 1
        if sum < 0:
            print('NO')
            break
    
    if sum > 0:
        print('NO')
    elif sum == 0:
        print('YES')