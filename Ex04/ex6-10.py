#-*- coding: utf-8 -*-
'''
Created on 2022. 7. 27.

@author: dhkdr
'''

# 정렬 실전문제2 (p179)
# 하나의 수열에는 다양한 수가 존재한다. 이러한 수는 크기에 상관 없이 나열되어 있다.
# 이 수를 큰 수부터 작은수의 순서로 정렬해야 한다. 수열의 내림차순으로 정렬하는 프로그램을 만드시오
# 입력조건, 출력조건 교재 p178 참고

#n을 입력받기
n = int(input())

#n개의 정수를 입력받아 리스트에 저장
array = []
for i in range(n):
    array.append(int(input()))

#파이썬 기본 정렬 라이브러리를 이용하여 정렬 수행    
array = sorted(array, reverse=True)

#정렬이 수행된 결과를 출력
for i in array:
    print(i, end=' ')