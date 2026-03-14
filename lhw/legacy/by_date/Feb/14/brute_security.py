# SWEA - 2117
# 홈 방범 서비스
# 2214

import sys
sys.stdin = open('z.txt')

def func(n, m, field):

    def cost(k):
        return K*K + (K-1)*(K-1)

    result = 0

    for K in range(1, 2*n + 2):
        fee = cost(K)

        for r in range(n):
            for c in range(n):
                houses = 0

                limit = K - 1
                for dx in range(-limit, limit+1):
                    rem = limit - abs(dx)
                    nr = r + dx
                    if 0 <= nr < n:
                        for dy in range(-rem, rem + 1):
                            nc = c + dy
                            if 0 <= nc < n and field[nr][nc] == 1:
                                houses += 1

                if houses * m >= fee:
                    result = max(result, houses)
    return result


T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    field = [list(map(int, input().split())) for _ in range(n)]

    print(f"#{tc} {func(n, m, field)}")


'''
### 완벽히 똑같은 로직, 전혀 다른 구현 방법
# 비교적 간단한 완전탐색 문제였기에 오늘 푼 다른 문제들보다는 수월했지만 해결하지는 못헀다.
# 완벽하게 똑같은 로직을 사용했는데 맨해튼 거리를 구현하는 방법에서 차이가 있었다.
# 나는 불필요하게 거리가 K에 해당하는 사각형을 전체 탐색하며 마름모를 탐색했는데
# 위 코드는 딱 필요한 마름모 만큼만 for문을 순회한다.

1. 맨해튼 거리 구현 코드
 # 위에 기술했듯이 차이가 느껴진다.
 # 외우자.

2. 이중함수
 # 이중함수가 종종 보이는데 위의 cost 함수는 사실 필요 없는 함수이기도 하다.
'''