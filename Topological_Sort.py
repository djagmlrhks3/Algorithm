from collections import deque

v, e = map(int, input().split())

# 진입차수
indegree = [0] * (v+1)
# 연결 리스트
graph = [[] for _ in range(v+1)]

for _ in range(e):
    start, end = map(int, input().split())
    graph[start].append(end)
    indegree[end] += 1

def topological_sort():
    result = []
    queue = deque()

    # 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v+1):
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        now = queue.popleft()
        result.append(now)
        # now와 연결된 노드들의 진입차수 -1
        for i in graph[now]:
            indegree[i] -= 1
            # 진입차수가 0이 되는 새로운 노드를 queue에 삽입
            if indegree[i] == 0:
                queue.append(i)

    for i in result:
        print(i, end=' ')

topological_sort()

# 입력
"""
7 8
1 2
1 5
2 3
2 6
3 4
4 7
5 6
6 4
"""
# 출력
"""
1 2 5 3 6 4 7
"""