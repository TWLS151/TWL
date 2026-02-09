import sys
sys.stdin = open('./input.txt', 'r')

T = int(input())

def portal(potal, N):

    # 1. 변수지정
    current_pos = 0                      # 현재 위치한 방
    count = 0                            # 포탈 사용 횟수
    used_portal = [0]*N                  # 해당 방의 포탈 사용 여부
    used_portal[0] = used_portal[-1] = 1 # 주의 1 : 시작, 끝 방은 돌아가는 영역에서 제외

    while current_pos < N-1:                 # 2. 현재 위치가 끝 방일 경우 종료

        if used_portal[current_pos] == 0:    # 3-1. 해당 방에 처음 도착한 경우
            used_portal[current_pos] += 1    # 해당 포탈의 사용 횟수 +1
            current_pos = potal[current_pos] # P[i]로 이동
            count += 1

        else:                                # 3-2. 해당 방에 가본 적 있는 경우 -> 다음 방으로 이동
            current_pos += 1
            count += 1

    return count


for tc in range(1, 2):

    N = int(input())
    portal_list = list(map(int, input().split()))
    result = portal(portal_list, N)

    print(f"#{tc} {result}")