import sys

input= sys.stdin.readline

A,B,C,M= map(int,input().split())

workout=0 #일한 양(B)
time=24 #남은 시간(하루종일)
tired_rate=0 #피로도

while time>0:
    if A>M: break
    if tired_rate+A<=M: #일 가능
        tired_rate+=A
        workout+=B
    else: #일 불가. 쉬어야함
        tired_rate-=C 
    time-=1

print(workout)