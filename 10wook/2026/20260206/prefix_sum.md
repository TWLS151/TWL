# 끝나지 않는 누적합


안녕하세요 목요일에 개념을 이해하고 쾌감을 레전드로 누린 한영욱입니다.

목요일에 개념 이해를 넘어서 문제 풀이도 직접하게 된 한영욱입니다.


하여 백준 두문제를 추가로 풀었습니다.

지금 코드 보여드릴게용


구간합 구하기 5 (11660)
```python
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
L = []
for _ in range(N):
    L.append(list(map(int,input().split())))    
# L은 N*N크기의 행렬입니다

#여기서 2차원 누적합을 구해줍니다.
prefix = [[0]*(N+1) for _ in range(N+1)]

#2차원 배열 채우기
for i in range(1,N+1):
    for j in range(1,N+1):
        prefix[i][j] = L[i-1][j-1] + prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1]
# print(prefix)
for _ in range(M) : 
    x1,y1,x2,y2 = map(int,input().split())
    #앞에 주어지는 애들이 무조건 작고, 지금의 경우에는 누적합에는 입력갑 그대로 계산해주면 되고, 뺄 친구는 -1씩 해준애로 계산하면 된다. 
    # 2차원 누적합 기본 공식은 포함 배제의 원래를 이용해서 pre[x2][y2] + pre[x1-1][y1-1] - pre[x2][y1-1]- pre[x1-1][y2]
    print(prefix[x2][y2] + prefix[x1-1][y1-1] - prefix[x2][y1-1]- prefix[x1-1][y2])

```
주지수 15724
```python
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
L = []
for _ in range(N):
    L.append(list(map(int,input().split())))    
# L은 N*N크기의 행렬입니다

#여기서 2차원 누적합을 구해줍니다.
prefix = [[0]*(M+1) for _ in range(N+1)]

#2차원 배열 채우기
for i in range(1,N+1):
    for j in range(1,M+1):
        prefix[i][j] = L[i-1][j-1] + prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1]
# print(prefix)
K = int(input())
for _ in range(K) : 
    x1,y1,x2,y2 = map(int,input().split())
    #앞에 주어지는 애들이 무조건 작고, 지금의 경우에는 누적합에는 입력갑 그대로 계산해주면 되고, 뺄 친구는 -1씩 해준애로 계산하면 된다. 
    # 2차원 누적합 기본 공식은 포함 배제의 원래를 이용해서 pre[x2][y2] + pre[x1-1][y1-1] - pre[x2][y1-1]- pre[x1-1][y2]
    print(prefix[x2][y2] + prefix[x1-1][y1-1] - prefix[x2][y1-1]- prefix[x1-1][y2])

```

목요일에 업로드 했던 2차원 누적합의 개념을 완벽하게 이해하고 손으로 직접 짜는 시간을 가졌습니다.


친구가 제공해준 누적합 문제를 골드 짜리가 하나 더 있는게 그건 시간 초과 메모리 초과 아주 난리 인 상태입니다.

그래서 이를 어떻게 해결할 수 있을지 생각해보고 있습니다.
지피티 피셜 새로운 개념을 적용해야한다고 하더군요.


그래서 그 개념을 공부해볼까 아니면, 누적합을 더 파볼지 고민중입니다.


토요일은 정처기 공부를 조지고, 일요일은 기출을 풀어보겠습니다.



그럼 오늘은 여기서 이만 입니다.