#-*- coding: utf-8 -*-
'''
Created on 2022. 7. 6.

@author: dhkdr
'''

# BFS
# 예제 : BFS (p147)

# 큐를 위해 deque 라이브러리 불러오기
from collections import deque

# BFS 함수 정의
def bfs(graph, start, visited): 
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start]) # 시작노드를 큐에 넣어줍니다.
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft() # 가장 먼저 들어왔던 원소를 꺼냄(popleft)
        print(v, end=' ') # 원소를 꺼낸 뒤 해당 노드의 번호를 출력해줌
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입 (꺼낸 노드와 인접한 노드를 하나씩 확인)
        for i in graph[v]:
            if not visited[i]: # 방문하지 않은 원소가 있어? 
                queue.append(i) 
                visited[i] = True # 방문처리를 해주세요

# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
  [], # 0번 노드는 비워주세요 (index 0에 대한 부분은 비워주세요, 보통 1부터 시작하는 경우가 있다보니 필요함)
  [2, 3, 8], # 1번 노드와 연결 (초기화 된 상태)
  [1, 7], # 2번 노드와 연결
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트) => 방문처리를 위한 1차원 리스트를 만들어줌
visited = [False] * 9 
# 기본 노드를 false로 초기화해놔서 하나도 방문하지 않은 상태로 만들어줌
# 0번 인덱스를 사용하지 않을거라 8+1 = 9로 설정해줌

# 정의된 BFS 함수 호출
bfs(graph, 1, visited)


# https://data-marketing-bk.tistory.com/45?category=901221 참고하기
# BFS를 구현하기 위해서는 항상 "방문하고자 하는 노드"와 "방문했던 노드"를 나누어서 알고리즘을 구성하는 것이 핵심 원리입니다. 