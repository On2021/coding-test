#-*- coding: utf-8 -*- 
'''
Created on 2022. 7. 4.

@author: dhkdr
'''
from bokeh.plotting import _stack

# 스택
# 예제 : 스택예제 (p126)

stack = []

#삽입5 - 삽입2 - 삽입3 - 삽입7 - 삭제 - 삽입1 - 삽입4 - 삭제
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack) # 최하단 원소부터 출력
print(stack[::-1]) # 최상단 원소부터 출력

# stack[::-1] : list의 인덱스에 접근하는 방법 Extended Slices
# -1은 처음부터 끝까지 -1칸 간격으로 (역순으로)
# stack[::2] : 처음부터 끝까지 2칸 간격으로
# stack[3::-1] : index3부터 끝까지 -1칸 간격으로 (역순으로)
# stack[1:6:2] : index1부터 index6까지 2칸 간격으로

# list 맨 끝에 항목 추가하기 append()
# 항목을 반환하면서, 리스트에서 값을 삭제하기 pop(), pop(인덱스)
# 그외 함수는 하단 링크 참고하기 
# https://vision-ai.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%A6%AC%EC%8A%A4%ED%8A%B8-%ED%95%AD%EB%AA%A9-%EC%B6%94%EA%B0%80-%EC%82%AD%EC%A0%9C
