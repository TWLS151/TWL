import sys

sys.stdin = open('./input.txt', 'r')

T = int(input())

for tc in range(1, T+1):

    N, k = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]

    block = 0                   # 블록 개수를 셀 변수 지정
    count = 0

    # [행 검사]
    for r in range(N):          # 행 전체에 대해 순회

        if count == k:          # 끝 인덱스를 탐색한 후 다음 행을 보기 전
            block += 1          # count = k이면 block에 1 추가

        count = 0               # 다음 행 : block 초기화

        for c in range(N):      # 요소를 순회
            if arr[r][c] == 1:  # 만약 1을 발견하면
                count += 1      # count를 1 증가

            else:               # 0을 만났을 때
                if count == k:  # 만약 count = k라면
                    block += 1  # block에 1을 증가

                count = 0       # count 초기화

    # [열 검사]
    for c in range(N):

        if count == k:          # 끝 인덱스를 탐색한 후 다음 행을 보기 전
            block += 1          # count = k이면 block에 1 추가

        count = 0

        for r in range(N):      # 요소를 순회
            if arr[r][c] == 1:  # 만약 1을 발견하면
                count += 1      # count를 1 증가

            else:               # 0을 만났을 때
                if count == k:  # count = k라면
                    block += 1  # block을 1 증가
                # 1이 아니면
                count = 0       # count 초기화

    if count == k:
        block += 1

    print(f"#{tc} {block}")