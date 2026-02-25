### 2026.02.25 
## DFS, BFS로 섬 문제 풀기

- DFS로 문제를 풀려고 함
- 목표는 DFS 함수를 재귀함수로 만들어 함수 하나로 문제를 해결하기
- 사고의 과정

    시작이 0,0   
    현재위치 방문 -> 현재 위치가 1인지 확인
-> 1이면 델타이동으로 1인 위치를 찾아서 섬인지를 확인
->이 과정을 반복하다가 더이상 1이 없으면 island +1
->1이 아니거나 방문한적이 있으면 다음 위치로

- 문제점 1 : 어디에서 island라는 변수에 1을 줄 것인지를 정하지 못함
- 문제점 2 : 다음 위치를 어디로 설정할 지에 대한 구체적인 방식을 생각하지 못함.
- 문제점 3 : 문제점 2에 의해 재귀함수를 돌릴때 경우의 수가 기하급수적으로 증가하여 시간이 오래 걸리는 문제 발생

- 하여 의견 교환 후에 2중 for문을 통해서 1이 나올 때만 dfs 함수를 호출하는 방법으로 변경
``` Python
def dfs(y,x):
    visited[y][x] = True
    dx=[-1,-1,0,1,1,1,0,-1]
    dy=[0,-1,-1,-1,0,1,1,1]

    for i in range(8):
        if 0<=x+dx[i]<N and 0<=y+dy[i]<M:
            if grid[y+dy[i]][x+dx[i]] == 1 and not visited[y+dy[i]][x+dx[i]]:
                dfs(y+dy[i],x+dx[i])



T=1
for tc in range(1,1+T):
    N, M = map(int, input().split())
    grid = [list(map(int, input())) for _ in range(N)]
    visited = [[False] * M for _ in range(N)] 
    island=0
    for y in range(N):
        for x in range(M):
            if grid[y][x] == 1 and not visited[y][x]:
                dfs(y,x)
                island+=1

print(island)
```


## 개선해야할 점
- 먼저 DFS, BFS 경험이 적어서 고려해야할 점을 충분히 고려하지 못함. 문제에 맞는 방식을 적용해야 하는데 하고 싶은 방식을 적용하려고 하는 과정에서 고려하지 못한 점들에 의하여 문제가 계속해서 발생함.
- 어떤 데이터를 보관하고 어떤 데이터를 변경해야하는지에 대한 생각이 아직 부족함.
- 각주를 달아서 사고의 과정을 코드에 보일 수 있게 하기