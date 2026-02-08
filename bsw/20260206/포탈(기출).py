import sys
sys.stdin = open('포탈.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    room_lst = [0] + list(map(int, input().split()))
    visit_count = [0] * (N + 1) # 각 방을 몇 번 밟았는지 기록
    current = 1 # 출발 방은 1번                
    steps = 0  # 총 포탈 이용수                
    while current < N: # 도착하기 전까지 반복
        steps += 1  # 일단 한 걸음~
        if current == 1: # 1번 방이면 바로 2번
            current = 2
            continue
        visit_count[current] += 1 # 왔다는 신호를 기록함.(1로)
        if visit_count[current] == 1: # 안 왔으면?
            current = room_lst[current] # 방 리스트의 위치로 이동
        else: # 이미 왔었으면?
            current += 1 # 오른쪽으로 1칸 이동

    print(f'#{tc} {steps}')

    # 근데 N번 방에 있는 숫자가 N보다 크면 오류가 발생 안하나?





    