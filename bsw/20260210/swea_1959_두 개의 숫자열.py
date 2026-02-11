import sys

sys.stdin = open('swea_1959_두 개의 숫자열.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    A_ = list(map(int, input().split()))
    B_ = list(map(int, input().split()))
    max_val = 0
    if len(A_) >= len(B_): # B가 더 길면 A가 이동, 반대 케이스는 반대로
        for i in range(len(A_) - len(B_) + 1):
            sum_ = 0
            for j in range(len(B_)):
                sum_ += B_[j] * A_[i + j]
            if max_val <= sum_:
                max_val = sum_
    else:
        for i in range(len(B_) - len(A_) + 1):
            sum_ = 0
            for j in range(len(A_)):
                sum_ += B_[i + j] * A_[j]
            if max_val <= sum_: # 최댓값이 있으면 대체
                max_val = sum_
    print(f'#{tc} {max_val}')

            