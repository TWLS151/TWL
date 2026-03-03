import sys

sys.stdin = open('swea_1979_어디에 단어가 들어갈 수 있을까.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for r in range(N): # 가로줄 검사
        cnt = 0
        for c in range(N):
            if arr[r][c] == 1:
                cnt += 1
                # 1인 경우 일단 카운트를 추가
            else: # 0일때
                if cnt == M: # 길이랑 똑같다면 
                    result += 1 # 결과값 1
                cnt = 0 # 1을 만나면 cnt 초기화
        if cnt == M: # 최종적으로도 한번 확인
            result += 1
    for c in range(N): # 세로줄도 마찬가지
        cnt = 0
        for r in range(N):
            if arr[r][c] == 1:
                cnt += 1
            else:
                if cnt == M:
                    result += 1
                cnt = 0
        if cnt == M:
            result += 1
    print(f'#{tc} {result}')