#-*- coding: utf-8 -*- 
'''
Created on 2022. 6. 15.

@author: dhkdr
'''
# 그리디
# 실전문제1 : 큰 수의 법칙 (p92-p95)
# 문제생략, 책 참고하기

#간단하게 푸는 답안 예시
#n,m,k를 공백으로 구분하여 입력받기 (5,8,3)
n,m,k = map(int, input().split())
#n개의 수를 공백으로 구분하여 입력받기 (2,4,5,4,6)
data = list(map(int,input().split()))

data.sort() #입력받은 수들 정렬하기
first = data[n-1] #가장 큰 수 (6)
second = data[n-2] #두 번째로 큰수 (5)

result = 0

while True:
    for i in range(k): #가장 큰 수를 k번 더하기
        if m == 0: #m이 0이라면 반복문 탈출
            break
        result += first
        m -= 1 #더할 때마다 m에서 1씩 빼기
    if m ==0: #m이 0이라면 반복문 탈출
        break
    result += second #두 번째로 큰 수를 한 번 더하기 
    m -= 1 #더할 때 마다 m에서 1씩 빼기
    
print(result) #최종 답안 출력

#답안 예시 - 반복되는 수열에 대해서 파악하기
#n2,m2,k2를 공백으로 구분하여 입력받기 (5,8,3)
n2,m2,k2 = map(int, input().split())
#n개의 수를 공백으로 구분하여 입력받기 (2,4,5,4,6)
data2 = list(map(int,input().split()))

data2.sort() #입력받은 수들 정렬하기
first2 = data2[n-1] #가장 큰 수 (6)
second2 = data2[n-2] #두 번째로 큰수 (5)

#가장 큰 수가 더해지는 횟수 계산
count2 = int(m2/(k2+1)) * k2
count2 += m2 % (k2+1)

result2 = 0
result2 += (count2) * first2 #가장 큰 수 더하기
result2 += (m2-count2) * second2 #두 번째로 큰 수 더하기

print(result2)
