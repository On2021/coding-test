#-*- coding: utf-8 -*- 
'''
Created on 2022. 6. 16.

@author: dhkdr
'''

# 구현
# 예제 : 시각 (p113-p114)

# 문제 풀이
# H를 입력받기
h = int(input())

count = 0
for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)