#-*- coding: utf-8 -*-
'''
Created on 2022. 7. 4.

@author: dhkdr
'''

# 재귀 함수
# 예제 : 재귀함수 - 오류관련 (p130)

def recursive_function():
    print('재귀 함수를 호출합니다.')
    recursive_function()

recursive_function()

# RecursionError: maximum recursion depth exceeded while calling a Python object
# 재귀(Recursion)의 최대 깊이를 초과했다고 오류메시지가 뜬다.(호출 횟수 제한 > 무한대로 재귀 호출을 진행할 수 없음)
# 그래서 재귀 함수를 문제 풀이에서 사용할 때는 재귀 함수가 언제 끝날지, 종료 조건을 꼭 명시해야함 => ex5-4 참고


  