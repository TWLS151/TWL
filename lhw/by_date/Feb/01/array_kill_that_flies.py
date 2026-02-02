# 파리 잡기 문제입니다.
# 전체 코드는 파일 하단부에 넣겠습니다.

'''
행렬문제

쉽지만은 않은 문제였습니다.
문제 특성상 분기처리를 해야하는데 분기처리 하기가 너무너무너무너무 귀찮아서 한번에 해결하려 머리를 써봤지만 결국 실패했습니다.
'''
try:
    if i-k <= 0 or j-k <= 0:
        raise IndexError("negative is not allowed")
    plus_sum += arr[i][j-k] + arr[i][j+k] + arr[i-k][j] + arr[i+k][j]
    
except IndexError:
    pass
'''
위 코드가 문제의 코드인데 인덱스가 음수로 넘어가면 리스트 끝부분이 인풋이 들어온다는 걸 알고
음수가 되면 에러처리를 하려고 머리를 써봤습니다만 그렇게되면 그 경우의 수 자체를 버리는 결과가 되어버려서 결국 포기했습니다.

그 과정에서 원래 몰랐던 raise 라는 기능을 알게되었고 이는 if 문에 넣어 조건이 달성되면 자동으로 에러를 띄우는 기능을 가지고 있었습니다.
자세히는 잘 모르지만 알아두면 어느정도 쓸모가 있어 보입니다.
'''

#-------------------------------------#
# 고수의 코드
# 전체적으로 십자형과 x형의 구분 없이 푸는 사람이 많았다.

T = int(input())
dirs = [
    [(-1,0),(1,0),(0,-1),(0,1)],   
    [(-1,-1),(1,-1),(1,1),(-1,1)]   
]
 
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
 
    for i in range(N):
        for j in range(N): # 행렬 생성
            for d in dirs: # d 는 총 두개로 plus 와 cross 두개
                s = arr[i][j] # 좌표 설정
                for l in range(1, M): # l 만큼 
                    for dx, dy in d: # 십자형, x자형 안에서 하나씩 x, y 꺼내고
                        ni, nj = i + dx*l, j + dy*l # l 에 곱해서 좌표에 가감 
                        if 0 <= ni < N and 0 <= nj < N: # 이때 좌표값이 범위를 벗어나면 버림
                            s += arr[ni][nj] # 좌표에 있는 파리의 수에 다른 곳 파리 수를 더함
                ans = max(ans, s) # 계산 할 때마다 비교 및 갱신
 
    print(f"#{tc} {ans}") # 출력

#-------------------------------------------#
# MY CODE

T = int(input()) # 테스트 케이스 개수

def plus(arr): # 십자 모양 스프레이 함수 정의
    plus = [] # 각 경우의 수 담을 리스트
    for i in range(len(arr)): 
        for j in range(len(arr[i])): # i, j 행렬 순회 이중 for 문
            plus_sum = arr[i][j] # 초기값 설정
            for k in range(1, M): # 반복문으로 M 범위 파리 수 합산
                # 각 인덱스가 음수이거나 리스트 범위를 초과하면 생략하도록 분기처리
                # 파이썬 특성상 리스트 인덱스가 음수가 되면 역순으로 탐색하기 때문에 생략해야함
                if i+k < N:
                    plus_sum += arr[i+k][j]
                if j+k < N:
                    plus_sum += arr[i][j+k]
                if i-k >= 0:
                    plus_sum += arr[i-k][j]
                if j-k >= 0:
                    plus_sum += arr[i][j-k]
            
            plus.append(plus_sum) # 경우의 수 리스트에 추가
    return max(plus) # 그 중 최대값 리턴

def x(arr): # x 모양 함수로 십자모양과 구조는 같으나 인덱스 계산 부분만 차이가 있음
    x = []
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            x_sum = arr[i][j]
            for k in range(1, M):
                if i+k < N and j+k < N:
                    x_sum += arr[i+k][j+k]
                if j+k < N and i-k >= 0:
                    x_sum += arr[i-k][j+k]
                if i-k >= 0 and j-k >= 0:
                    x_sum += arr[i-k][j-k]
                if j-k >= 0 and i+k < N:
                    x_sum += arr[i+k][j-k]
            x.append(x_sum)
    return max(x)


for test_case in range(1, T+1): # 반복 및 테스트 케이스 출력을 위한 반복문
    N, M = map(int, input().split()) # N 과 M 입력
    arr = [list(map(int, input().split())) for _ in range(N)] # 컴프리헨션을 이용한 주어진 행렬 입력

    # 각 함수 호출
    fly_plus = plus(arr)
    fly_x = x(arr)

    # 둘 중 더 큰 값 출력
    print(f'#{test_case} {max(fly_plus, fly_x)}')




# 더미가 된 코드 #

# T = int(input())

# def plus(arr):
#     plus = []
#     for i in range(len(arr)):
#         for j in range(len(arr[i])):
#             plus_sum = arr[i][j]    
#             for k in range(1, M):
#                 try:
#                     if i-k <= 0 or j-k <= 0:
#                         raise IndexError("negative is not allowed")
#                     plus_sum += arr[i][j-k] + arr[i][j+k] + arr[i-k][j] + arr[i+k][j]
                    
#                 except IndexError:
#                     continue
#             plus.append(plus_sum)
#     return max(plus)

# def x(arr):
#     x = []
#     for i in range(len(arr)):
#         for j in range(len(arr[i])):
#             x_sum = arr[i][j]
#             for k in range(1, M):
#                 try:
#                     if i-k <= 0 or j-k <= 0:
#                         raise IndexError("negative is not allowed")
#                     x_sum += arr[i+k][j-k] + arr[i+k][j+k] + arr[i-k][j-k] + arr[i-k][j+k]
                    
#                 except IndexError:
#                     continue
#             x.append(x_sum)
#     return max(x)


# for test_case in range(1, T+1):
#     N, M = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(N)]

#     # 스프레이 로직
#     # 시작하는 칸 포함 M 칸 만큼 + 혹은 x 로 분사
#     # 그 칸 안에 있는 파리의 총합의 최대값
#     # 브루트포스?
#     fly_plus = plus(arr)
#     # print(fly_plus)
#     fly_x = x(arr)
#     # print(fly_x)


#     print(f'#{test_case} {max(fly_plus, fly_x)}')
#     # print(max(fly_plus, fly_x))