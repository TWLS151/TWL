# 위상정렬

DAG(Directed Acyclic Graph)에서 사용가능

개념
진입 차수 계산: 각 노드로 들어오는 화살표의 개수를 센다.
큐 활용: 진입차수가 0인 도느를 큐에 넣는다.
반복수행을 한다.

```py
from collections import deque

# n: 노드 수, graph: 인접 리스트, indegree: 진입 차수 리스트
def topological_sort(n, graph, indegree):
    result = []
    queue = deque([i for i in range(1, n + 1) if indegree[i] == 0])

    while queue:
        now = queue.popleft()
        result.append(now)
        
        for neighbor in graph[now]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
                
    return result
```