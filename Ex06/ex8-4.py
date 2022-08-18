#-*- cording:utf-8 -*-
'''
Created on 2022. 8. 18.

@author: dhkdr
'''

# 피보나치 수열 소스코드(반복적)
# 연습문제 8-4

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 100

# 첫번째 피보나치 수와 두번째 피보나치 수는 1
d[1] = 1
d[2] = 1
n = 99

# 피보나치 함수(Fibonacci Function) 반복문으로 구현(보텀업 다이나믹 프로그래밍)
for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]
    
print(d[n])