baekjoon link: https://www.acmicpc.net/problem/18258
---  

## Jieon
- 처음에 큐 클래스 안의 필드를 리스트를 이용해서 구현했더니 시간초과가 발생했다.
- 그래서 필드를 리스트에서 deque(덱)으로 변경하고 덱에 포함된 메서드를 이용해서 pop(사실 popleft)를 구현했더니 시간초과가 발생하지 않게 되었다.
- queue를 구현하는 문제인데 deque를 사용해도 될지 모르겠다... ㅋㅋ 애매쓰 

## Yeojoo
- 앞으로 input()은 거의 sys.stdin.readline()로 쓴다고 생각해야겠다ㅋㅋㅋㅋ
- deque로도 풀 수가 있구나...! 나두 그방법으로도 풀어봐야겠다.
