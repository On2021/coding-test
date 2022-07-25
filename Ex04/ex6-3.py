#-*- coding: utf-8 -*-
'''
Created on 2022. 7. 25.

@author: dhkdr
'''

# 정렬 - 삽입정렬
# 예제 : 삽입 정렬 소스코드 (p164)

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1): # 인덱스 i부터 1(0+1)까지 1씩 감소하며 반복하는 문법
        if array[j] < array[j-1]: # 한 칸씩 왼쪽으로 이동
            array[j], array[j-1] = array[j-1], array[j] # 스와프
        else: # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
            break
print(array)

# range의 세 번째 매개 변수
# range의 매개 변수는 3개(start, end, step)이다.
# 세 번째 매개 변수인 step에 -1이 들어가면 start 인덱스부터 시작해서 end+1 인덱스까지 1씩 감소한다.