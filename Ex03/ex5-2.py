#-*- coding: utf-8 -*-
'''
Created on 2022. 7. 4.

@author: dhkdr
'''

# 큐
# 예제 : 큐예제 (p129)

# 큐 구현을 위해 deque 라이브러리 사용
from collections import deque
queue = deque()

# 삽입5 - 삽입2 - 삽입3 - 삽입7 - 삭제 - 삽입1 - 삽입4 - 삭제
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) # 먼저 들어온 순서대로 출력
queue.reverse() # 다음 출력을 위해 역순으로 바꾸기
print(queue) # 나중에 들어온 원소부터 출력

# deque는 스택과 큐의 장점을 모두 채택한 것, 데이터를 넣고 빼는 속도가 리스트 자료형에 비해 효율적이다.
# deque는 import해서 사용해야한다.
# deque에 존재하는 메서드는 하단 링크를 참고하자
# https://leonkong.cc/posts/python-deque.html

# deque 객체를 리스트 자료형으로 변경하고자 한다면 list() 메서드를 이용!
list(queue) # 이렇게 입력하면 리스트 자료형이 반환된대!

