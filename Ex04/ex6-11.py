#-*- coding: utf-8 -*-
'''
Created on 2022. 7. 28.

@author: dhkdr
'''

# 정렬 실전문제3 (p181)
# n명의 학생 정보가 있다. 학생 정보는 학생의 이름과 학생의 성적으로 구분된다.
# 각 학생의 이름과 성적 정보가 주어졌을 때 성적이 낮은 순서대로 학생의 이름을 출력하는 프로그램 작성
# 입력,출력조건은 교재 p180 참고

#n을 입력받기
n = int(input())

#n명의 학생정보를 입력받아 리스트에 저장
array = []
for i in range(n):
    input_data = input().split()
    #이름은 문자열 그대로, 점수는 정수형으로 변환하여 저장
    array.append((input_data[0], int(input_data[1])))
    
#key를 이용하여, 점수를 기준으로 정렬
array = sorted(array, key=lambda student: student[1])

#정렬이 수행된 결과를 출력
for student in array:
    print(student[0], end=' ')