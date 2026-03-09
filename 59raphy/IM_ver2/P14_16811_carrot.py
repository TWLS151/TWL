import sys

sys.stdin = open('input_p14_carrot.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    C = list(map(int, input().split()))
    C.sort()  # 당근 크기순 정렬

    M = N // 2   # 한 상자에 담을 수 있는 최대 개수
    min_dif = N  # 최소 차이 초기값 설정

    # 첫 번째 경계 i (소 상자의 당근 개수와 동일)
    # 소 상자 개수 조건(1 <= i <= M)에 따라 i 범위 설정
    for i in range(1, M + 1):

        # 소, 중 상자의 경계면 값이 같으면 같은 크기가 분리된 것이므로 무효
        if C[i-1] == C[i]:
            continue

        # 두 번째 경계 j (중 상자까지의 누적 당근 개수와 동일)
        # 중 상자 개수: j-i, 대 상자 개수: N-j
        # 대 상자 개수 조건(1 <= N-j <= M)에 따라 j 범위 설정: N-M <= j <= N-1
        for j in range(N - M, N):

            # 중 상자가 비어있거나(j-i==0), M을 초과할 경우 무효
            # N이 짝수인 경우 M == N-M이므로 i와 j 값이 같아질 수 있음
            if i == j or j - i > M:
                continue

            # 중, 대 상자의 경계면 값이 같으면 같은 크기가 분리된 것이므로 무효
            elif C[j-1] == C[j]:
                continue

            # 조건을 모두 만족하는 경우 세 상자의 개수 차이 계산 및 최솟값 갱신
            else:
                boxes = [i, j-i, N-j]
                dif = max(boxes) - min(boxes)
                if min_dif > dif:
                    min_dif = dif

    # 탐색 후에도 min_dif가 갱신되지 않았다면 포장 불가(-1)
    if min_dif == N:
        min_dif = -1

    print(f'#{tc} {min_dif}')


#=================================================================
# ver_1
# 260211

    """

    Ci.sort()
    
    # 결과값 초기화
    min_diff = N
    L = N // 2

    # 첫 번째 경계선 i (소형 상자의 마지막 인덱스)
    for i in range(1, N - 1):
        # 두 번째 경계선 j (중형 상자의 마지막 인덱스)
        for j in range(i + 1, N):
            # 1) 경계 지점의 당근 크기가 다음 당근과 다르다면
            if Ci[i - 1] != Ci[i] and Ci[j - 1] != Ci[j]:
                
                # 각 상자의 당근 개수 계산
                small_cnt = i
                medium_cnt = j - i
                large_cnt = N - j
                
                # 2) 모든 상자가 N//2를 초과하지 않는다면
                if small_cnt <= L and medium_cnt <= L and large_cnt <= L:
                    # 현재 조합의 최대-최소 차이 계산
                    diff = max(small_cnt, medium_cnt, large_cnt) - min(small_cnt, medium_cnt, large_cnt)
                    
                    # 최솟값 갱신
                    if diff < min_diff:
                        min_diff = diff

    # 조건을 만족하는 경우가 한 번도 없어서 min_diff가 갱신되지 않았다면 -1 반환
    result = min_diff if min_diff != N else -1
    
    print(f'#{tc} {result}')
    """
