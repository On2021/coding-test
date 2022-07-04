#-*- coding: utf-8 -*-
'''
Created on 2022. 7. 4.

@author: dhkdr
'''

# 재귀 함수
# 예제 : 재귀함수 - 종료 조건(p131-p132)

def recursive_function(i):
    if i==100:
        return
    print(i,'번째 재귀 함수에서',i+1,'번째 재귀 함수를 호출합니다.')
    recursive_function(i+1) # 여기부분이 왜 99 > 1로 -1씩되서 출력되는지 모르겠음(?)
    print(i,'번째 재귀 함수를 종료합니다.')
    
recursive_function(1)

# 팩토리얼(Factorial)로 재귀 함수 풀기
# 예제 : 재귀함수 - 팩토리얼(p132-p133)

def factorial_iterative(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result

# 재귀적으로 구현한 n!
def factorial_recursive(n):
    if n <= 1:
        return 1
    #n! = n * (n-1)!를 그대로 코드로 작성하기
    return n * factorial_recursive(n-1)

# 각각의 방식으로 구현한 n! 출력(n=5)
print('반복적으로 구현:',factorial_iterative(5))
print('재귀적으로 구현:',factorial_recursive(5))

