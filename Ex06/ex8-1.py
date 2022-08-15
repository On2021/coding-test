#-*- cording:utf-8 -*-

'''
Created on 2022. 8. 15.

@author: dhkdr
'''

# 피보나치 함수
# 연습문제 8-1 : 피보나치 함수 소스코드

# 피보나치 함수(Fibonacci Function)를 재귀 함수로 구현
def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x-1) + fibo(x-2)

print(fibo(4))

'''
그런데 이렇게 소스코드 작성하면 심각한 문제 발생할 수 있음
f(n)함수에서 n이 커지면 커질수록 수행 시간이 기하급수적으로 늘어나기 때문
교재 p211 이미지 참고
이미 한번 계산했지만, 계속 호출할 때마다 계산하기 때문에 문제가 발생함.
'''