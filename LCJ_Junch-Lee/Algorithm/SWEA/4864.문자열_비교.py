import sys
sys.stdin = open('input.txt','r')

T = int(input())

def is_in_pattern(p, t):

    N = len(p)
    M = len(t)

    count = 0
    result = False

    i = 0
    j = 0

    while i < M and j < N:

            if p[j] != t[i]:    # 불일치 시
                i = i - j + 1   # 비교 시작 위치 +1 칸
                j = 0           # 패턴의 처음부터 비교 시작
                count = 0       # count 초기화

            else:
                i += 1
                j += 1
                count += 1


            if count == N:
                result = True
                break
    return int(result)

for tc in range(1, T+1):

    p = input()
    t = input()

    print(f"#{tc} {is_in_pattern(p,t)}")