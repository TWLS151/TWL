import sys
sys.stdin = open('input.txt', 'r')

# 문제 풀이 포인트
# 1. 교착 상태 : 1-N극, 2-S극이 맞붙은 상태
# 카운팅 기준 : 1-2가 교차되어 나타날 때 교착 +1 

# 2. 순회 기준? 
# 열 -> 행으로 시도

# 3. 탐색 과정?
# (1) 0은 건너뛰기
# (2) if arr[r][c] != 0 -> 세부 탐색
# (2)-1. 1을 만났을 때 
# --> range(r+1 ~ N): 아래에 2가 있는 경우에 deadlock += 1

# 카운팅을 해준다면? 
# if 1 만나면 north = True
# -> 2 만나고, north = True : deadlock + 1 , North = False

# else (2)-2. 2를 먼저 만나면 -> skip

def find_deadlock(arr, N):

    deadlock = 0 # 교착 상태
    north = False # 초기 : N극(1)을 만나지 않음

    for c in range(N): # 열 우선순회 
        north = False  # 열 바뀌면 다시 초기화
        for r in range(N):

            if arr[r][c] != 0: # 0이 아닐 경우 (탐색 시작)

                if north and arr[r][c] == 2 : # N극이 위에 있고, 2를 만나면 
                    deadlock += 1             # 교착 +1 
                    north = False
            
                elif arr[r][c] == 1:# 위에 N극이 없거나, 있는데 1을 만난 경우 (예외처리)
                    north = True

    return deadlock

for tc in range(1,11): 

    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    result = find_deadlock(arr, N)

    print(f"#{tc} {result}") 