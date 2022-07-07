#-*- coding: utf-8 -*-
'''
Created on 2022. 7. 7.

@author: dhkdr
'''
# BFS/DFS
# 실전 : BFS/DFS - 음료수 얼려 먹기 (p149-p151)

# N, M을 공백을 기준으로 구분하여 입력 받기 
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))
# 이 때 입력은 공백 없이 0과 1로 구성된 문제 형태로 주어짐 => 한 줄 입력받은 다음에 각 원소를 정수형으로 바꿔서 리스트 형태로 바꿔줌 => 0,1 정수로 들어감 

# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] = 1
        # 상, 하, 좌, 우의 위치들도 모두 재귀적으로 호출
        # 상, 하, 좌, 우로 호출되는 내용들은 리턴값을 사용하지 않기 때문에 단순히 연결된 노드에 대해서 방문 처리를 수행하기 위한 목적으로 사용됨
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

# 모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i, j) == True: # 방문처리가 됐다면
            result += 1 # 그때 카운팅 처리를 해줘욥

print(result) # 정답 출력

# 이 문제는 연결 요소를 찾는 문제다. (한 번에 만들 수 있는 아이스크림 개수를 출력하기)
# 방문처리가 된 요소만 찾아서 카운트하면 됨