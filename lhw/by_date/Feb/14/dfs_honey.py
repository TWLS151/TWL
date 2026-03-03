# SWEA - 2115
# 벌꿀채취
# https://velog.io/@hyunsoo730/SWEA-2115-%EB%B2%8C%EA%BF%80%EC%B1%84%EC%B7%A8-Python-gtapnurg

import sys
sys.stdin = open('z.txt')

def dfs(l, r, c, now, val):  # 작업구역 길이, 시작 행, 열, 지금까지 선택한 값의 합, 수익
    global revenue
    if now > C:  # C가 넘어가면 가지치기
        return
    if l == M:  # 작업구역 길이가 제한에 닿으면
        revenue = max(revenue, val)  # 수익 계산
    else:
        dfs(l + 1, r, c+1, now + honey[r][c], val + honey[r][c]**2)  # 지금 위치를 고르는 것
        dfs(l + 1, r, c+1, now, val)  # 안고르는 것


T = int(input())

for t in range(1, T+1):
    N, M, C = map(int, input().split())
    honey = [list(map(int, input().split())) for _ in range(N)]

    revenue = 0  # 수익
    revenue_a = 0  # a의 수익
    revenue_b = 0  # b의 수익
    result = 0  # a와 b의 합

    # a의 구역을 정한다.
    for r1 in range(N):
        for c1 in range(N-M+1):
            revenue = 0
            dfs(0, r1, c1, 0, 0)
            revenue_a = revenue
            
            # b의 구역을 정한다.
            for r2 in range(r1, N):  # A의 구역과 겹치지 않도록 
                start = 0
                if r1 == r2:  # A의 시작 열과 겹치면
                    start = c1 + M  # 같은 행의 c1 + M 이 a의 작업이 끝나는 곳이니 거기부터 시작
                for c2 in range(start, N-M+1):  # 순회
                    revenue = 0  
                    dfs(0, r2, c2, 0, 0)
                    revenue_b = revenue

                    result = max(result, revenue_a + revenue_b)
    
    print(f'#{t} {result}')


'''
이 문제도 DFS 라고 생각 못했다.

1. 작업 구역을 나누지 못헀다.
 # 문제에서 A와 B의 작업구역이 겹치면 안된다는 조건이 있어 나는 방문처리와 비슷하게
 # A가 작업하는 구역을 마스킹 해놓고 그 부분 밖으로 B가 작업을 하도록 설계했는데
 # 설계대로 잘 되지 않았다.
 # 위 코드에서는 간단하게 if 문 하나로 똑같은 설계를 성공했다.

2. DFS 설계를 생각하지 못헀다.
 # 함수를 하나 짜긴 했는데 DFS 함수는 아니었고 완전탐색 함수였다.
 # 완전탐색을 하지 못하는 완전탐색이었다는게 문제.

3. 글로벌 변수 사용을 꺼리지 말자
 # 좋지 않다는 건 알겠다. 그래서 어떻게 안쓰는데?
 # 아직 나 그 수준 아니다. 그냥 되는대로 다 갖다 쓰자.
'''


'''
오늘 이 문제가 6번째 알고리즘인데 하면서 느낀점이 있다.
최근에 코드가 안돌아가는 일이 줄었다는 점이다.
일단 정답을 뽑아내진 못하지만, 생각과는 다르더라도 결과를 뱉긴 한다.
과정에서 에러가 완전히 없는건 아니지만 그래도 더 나아진건가 싶은 생각을 한다.
'''