#-*- coding: utf-8 -*-
'''
Created on 2022. 8. 3.

@author: dhkdr
'''

# 이진탐색 예제2 (p189)

#이진 탐색 소스코드 재현(재귀 함수)
def binary_search(array, target, start, end):
    if start > end:
        return None #시작점의 위치가 끝점의 위치를 벗어날 때
    mid = (start + end) // 2 #중간점을 의미함
    
    #찾은 경우 중간점 인덱스 반환
    if array[mid] == target: #타겟값을 찾은 경우, 타겟 값의 위치가 중간점일 때
        return mid #중간점의 위치 반환
    
    #중간점의 값보다 찾고자 하는 값이 적은 경우 왼쪽 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1) #중간점의 왼쪽 탐색
    
    #중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return binary_search(array, target, mid+1, end) #중간점의 오른쪽 탐색
    
#n(원소의 개수)과 target(찾고자 하는 문자열)을 입력받기
n, target = list(map(int,input().split()))
#전체 원소 입력 받기
array = list(map(int,input().split()))

#이진 탐색 수행 결과 출력
result = binary_search(array,target,0,n-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result+1)
    
    