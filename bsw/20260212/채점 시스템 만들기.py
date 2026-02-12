import sys

sys.stdin = open('채점 시스템 만들기.txt')
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    solution = list(map(int, input().split()))
    stu_s_ = [list(map(int, input().split())) for _ in range(N)]
    max_val = 0 
    min_val = float('inf') # 최댓값 최솟값 지정
    for j in range(N):
        add_num = 0
        sum_ = 0
        for i in range(M):
            if stu_s_[j][i] == solution[i]:
                add_num += 1
                sum_ += add_num # 더하는 수를 0으로 처음에 정하고 1씩 증가시키며 더하기
            else:
                add_num = 0

        if max_val < sum_:
            max_val = sum_
        if min_val > sum_:
            min_val = sum_ # 더 작거나 큰 값 나오면 대체
    print(f'#{tc} {max_val - min_val}')
