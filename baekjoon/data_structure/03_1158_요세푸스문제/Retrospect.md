baekjoon link: https://www.acmicpc.net/problem/1158
---  

## Jieon
- 처음에 환형큐(circular queues)를 class로 구현하려고 했다. 그런데 찾아보니 python deque 클래스에 rotate라는 아주 좋은 메소드가 있었다.
- rotate는 큐를 회전해주는 역할을 한다. 
- q: [ 1,2,3,4,5 ] 일 경우, q.rotate(2)를 하면, [ 4,5,1,2,3 ]이 된다. q.rotate(-2)를 하면, [ 3,4,5,1,2]가 된다. 순서에 주의해야 한다.
 
## Yeojoo
- 리스트로 구하려구 노트에 적으면서 풀었다ㅋㅋㅋ
- deque의 rotate 사용하는게 제일 깔끔하겠구만
