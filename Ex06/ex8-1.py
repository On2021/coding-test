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