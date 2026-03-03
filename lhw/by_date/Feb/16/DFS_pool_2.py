# SWEA - 1952
# 수영장
# 2회차 - 그리드로 풀었던거 dfs 로 풀어보기

import sys
sys.stdin = open('input.txt')


def dfs(moon, val):
    global fee, kekaku, best
    # 기저조건
    # 12월까지 다 보면 종료
    if moon > 11:
        best = min(best, val)
        return

    # 할 일
    # 매 달 모든 선택
    backup = val

    # 일단 사용하는 달만
    # 일일
    val += kekaku[moon] * fee[0]
    dfs(moon + 1, val)
    val = backup

    # 한달
    if kekaku[moon] > 0:
        val += fee[1]
        dfs(moon + 1, val)
        val = backup
        # 세달
        val += fee[2]
        dfs(moon + 3, val)
        val = backup



TC = int(input())
for test_case in range(1, TC+1):
    fee = list(map(int, input().split()))
    kekaku = list(map(int, input().split()))

    # 가장 적게 지출하는 비용
    # 매 달 선택을 한다
    # 일일 한달 세달 일년
    best = fee[3]

    dfs(0, 0)

    print(f'#{test_case} {best}')
    