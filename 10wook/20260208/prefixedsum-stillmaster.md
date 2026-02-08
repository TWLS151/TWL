# 아직도 2중 누적합이다.


## 2167번을 풀었습니다. 난이도를 높이고 싶은데 조금만 변수가 나오면 못 풀겠더군요....


이후에는 다음은 BFS로 넘어가든가 하고자합니다.

암튼 금일 풀이였습니다
``` python
N,M = map(int,input().split())
L = []
for i in range(N):
    L.append(list(map(int,input().split())))
prefixed = [[0]*(M+1) for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,M+1):
        #내 원래 자리 더하고, 대각선 뒤에 빼고 양 옆 더 해준다.
        prefixed[i][j] = L[i-1][j-1] + prefixed[i-1][j] + prefixed[i][j-1] - prefixed[i-1][j-1]
# print(prefixed)
A = int(input())
for i in range(A):
    x1, y1, x2, y2 = map(int,input().split())
    #내가 원하는 모양으로 짜르고,포함 배제의 원리로 더 할거 더 해 줌
    print(prefixed[x2][y2] - prefixed[x2][y1-1] - prefixed[x1-1][y2] + prefixed[x1-1][y1-1])
```