#-*- coding: utf-8 -*-
'''
Created on 2022. 7. 25.

@author: dhkdr
'''

# 정렬 - 선택정렬
# 예제 : 선택 정렬 소스코드 (p159)

# 0-9까지의 수가 무작위로 array 안에 있다.
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# 반복문을 이용한다.
for i in range(len(array)): # i가 array의 길이만큼 반복하는데
    min_index = i # 가장 작은 원소의 인덱스 = i
    for j in range(i + 1, len(array)): # j가 array의 길이만큼, i+1부터 반복한다
        if array[min_index] > array[j]: # 근데 array의 min_index가 array의 j보다 크면
            min_index = j # j를 min_index에 넣는다
    array[i], array[min_index] = array[min_index], array[i] # 스와프
    # 파이썬에서는 윗줄처럼 간단히 리스트 내 두 원소의 위치를 변경할 수 있다.
    
print(array)

