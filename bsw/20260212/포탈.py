import sys

sys.stdin = open('포탈.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    pt_lst = list(map(int, input().split()))
    cur_loc = 0 # 현재 위치를 지정
    cnt = 0 # 카운트 지정
    visited = [0] * N # 방문 여부 리스트 설정
    while cur_loc != N - 1: # N-1의 인덱스가 cur_loc와 같아야 끝방 도달하므로
        if pt_lst[cur_loc] == 0:
            cur_loc += 1
            cnt += 1
            # 1번방은 무조건 오른쪽으로 이동
        else:
            if visited[cur_loc] == 1:
                cur_loc += 1
                cnt += 1
            # 방문했던 곳이면 1 이동
            else:
                move = pt_lst[cur_loc] 
                cnt += 1 
                visited[cur_loc] += 1 # 방문 기록
                cur_loc = move - 1
                # 현재 위치에서 -1을 뺀 값만큼 현재 위치 갱신(인덱스 때문)
    print(f'#{tc} {cnt}')
