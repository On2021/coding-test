#-*- coding: utf-8 -*-
'''
Created on 2022. 7. 6.

@author: dhkdr
'''

# DFS/BFS
# 예제 : DFS - 인접 행렬 방식 (p135)

INF = 999999999 # 무한의 비용 선언

# 2차원 리스트를 이용해 인접 행렬 표현
graph = [
    [0,7,5],
    [7,0,INF],
    [5,INF,0]
]

print(graph)