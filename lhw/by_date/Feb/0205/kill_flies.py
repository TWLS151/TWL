# SWEA - 12712

# 누적합으로 풀기
# 누적합 개념부터 조금 다시 보고 오자

# 누적합 배열을 우선 만들어야겠네?

tc = int(input())

for test_case in range(1, tc+1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    # 파리 배열 만들었고

    sum_matrix = [[0]*N for _ in range(N)]
    # 누적합 넣을 배열 만들었고

    sum_matrix[0][0] = matrix[0][0]
    # 시작점 할당해주고

    # 첫행하고 첫열은 다 할당해줘야겠는데?
    for r in range(1, N):
        sum_matrix[r][0] = matrix[r][0] + matrix[r-1][0]

    for c in range(1, N):
        sum_matrix[0][c] = matrix[0][c] + matrix[0][c-1]
    
    #이제 칸 채우자
    for r in range(1, N):
        for c in range(1, N):
            sum_matrix[r][c] = matrix[r][c] + sum_matrix[r-1][c] + sum_matrix[r][c-1] - sum_matrix[r-1][c-1]

    # 확인
    # print((sum_matrix)) # 완성

    # 그럼 이제 지정하는 칸의 값을 구해내야하는데
    # 식 재배치?
    matrix[r][c] = sum[r][c] + sum[r-1][c-1] - sum[r-1][c] - sum[r][c-1]
    
    # 십자는 그렇다 치더라도 크로스는 하나하나 구해야할 거 같은데
    
























# # 이전에는 델타를 안쓰고 분기처리로 풀었는데
# # 지금은 델타를 배웠으니 델타를 활용해서 풀어보자 !

# # 함수 정의
# def killing_machine(arr, area):
#     pass
#     N = len(arr)

#     # 상하좌우
#     # 우상 좌상 우하 좌하
#     dirs = [
#         [(-1, 0), (1, 0), (0, -1), (0, 1)],
#         [(-1, -1), (-1, 1), (1, -1), (1, 1)]
#     ]
		
#     max_total = 0
#     # 배열 순회
#     for row in range(N):
#         for col in range(N):
#             px, py = row, col  # 타겟 좌표

#             # 모양 순회
#             for shape in dirs:
# 		        # 모양이 바뀌면 토탈값도 청소해야한다!
#                 total = arr[px][py]
#                 # 방향 순회
#                 for i in shape:
#                     dx, dy = i      # 방향 좌표

#                     # 타겟 좌표 제외하고 M 만큼 이동하며 기록
#                     for tempt in range(1, area):
# 		                    # 좌표가 필드 안에 있을 때만 계산 진행
#                         if 0 <= px + dx * tempt < N and 0 <= py + dy * tempt < N:
#                             total += arr[px + dx * tempt][py + dy * tempt]
								
# 								# 모양 바꾸기 전에 맥스 합계값 갱신
#                 if max_total < total:
#                     max_total = total
# 		# 반환
#     return max_total

# tc = int(input())

# for test_case in range(1, tc + 1):
#     N, M = map(int, input().split())
#     field = [list(map(int, input().split())) for _ in range(N)]

# 		# 출력
#     print(f'#{test_case}', killing_machine(field, M))




# T = int(input())

# def plus(arr):
#     plus = []
#     for i in range(len(arr)):
#         for j in range(len(arr[i])):
#             plus_sum = arr[i][j]    
#             for k in range(1, M):
#                 if i+k < N:
#                     plus_sum += arr[i+k][j]
#                 if j+k < N:
#                     plus_sum += arr[i][j+k]
#                 if i-k >= 0:
#                     plus_sum += arr[i-k][j]
#                 if j-k >= 0:
#                     plus_sum += arr[i][j-k]
            

#                 # try:
#                 #     if i-k <= 0 or j-k <= 0:
#                 #         raise IndexError("negative is not allowed")
#                 #     plus_sum += arr[i][j-k] + arr[i][j+k] + arr[i-k][j] + arr[i+k][j]
                    
#                 # except IndexError:
#                 #     continue
#             plus.append(plus_sum)
#     return max(plus)

# def x(arr):
#     x = []
#     for i in range(len(arr)):
#         for j in range(len(arr[i])):
#             x_sum = arr[i][j]
#             for k in range(1, M):
#                 if i+k < N and j+k < N:
#                     x_sum += arr[i+k][j+k]
#                 if j+k < N and i-k >= 0:
#                     x_sum += arr[i-k][j+k]
#                 if i-k >= 0 and j-k >= 0:
#                     x_sum += arr[i-k][j-k]
#                 if j-k >= 0 and i+k < N:
#                     x_sum += arr[i+k][j-k]
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