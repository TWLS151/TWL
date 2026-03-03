
swea5189
```python
T = int(input())
for test_num in range(1,1+T):


    graph = {}
    a,b = map(int,input().split())
    L = list(map(int,input().split()))
    # print(L)
    for i in range(0,2*a,2):
        if graph.get(L[i]):
            graph[L[i]] = graph[L[i]] + [L[i+1]]
        else:
            graph[L[i]] = [L[i+1]]
    S = []
    answer = 0
    S.append(b)
    while S:
        answer +=1
        visit = S.pop(0)
        if graph.get(visit):
            for i in graph[visit]:
                S.append(i)
        

    print(f'#{test_num} {answer}')


```





swea4012
```python
from itertools import combinations

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    synergy = [list(map(int,input().split())) for _ in range(N)]

    answer = float('inf')

    for team1 in combinations(range(N), N//2):
        team2 = [i for i in range(N) if i not in team1]

        s1 = 0
        s2 = 0

        for i in range(N//2):
            for j in range(i+1, N//2):
                a,b = team1[i], team1[j]
                s1 += synergy[a][b] + synergy[b][a]

                c,d = team2[i], team2[j]
                s2 += synergy[c][d] + synergy[d][c]

        answer = min(answer, abs(s1-s2))

    print(f'#{tc} {answer}')


```
