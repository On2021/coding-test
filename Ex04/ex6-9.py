#-*- coding: utf-8 -*-
'''
Created on 2022. 7. 26.

@author: dhkdr
'''

# 정렬 - sorted 정렬라이브러리
# 예제 : sorted 소스코드 (p176-177)

array = [('바나나',2),('사과',5),('당근',3)]

def setting(data):
    return data[1]
result = sorted(array, key=setting)
print(result)

# sorted()나 sort()를 이용할 때에는 key 매개변수를 입력으로 받을 수 있다.
# key값으로는 하나의 함수가 들어가야 하며 이는 정렬 기준이 된다.