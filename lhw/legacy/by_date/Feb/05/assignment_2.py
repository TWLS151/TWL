OFFSET = 1000
MAX_R = 2000

# 변수 선언 및 입력
n = int(input())
segments = []

# 현재 위치
cur = 0

for _ in range(n):
	distance, direction = tuple(input().split())
	distance = int(distance)
	
	if direction == 'L':
		# 왼쪽으로 이동할 경우 : cur - distance ~ cur까지 경로 이동
		section_left = cur - distance
		section_right = cur
		cur -= distance
	else:
		# 오른쪽으로 이동할 경우 : cur ~ cur + distance까지 경로 이동
		section_left = cur
		section_right = cur + distance
		cur += distance
	
	segments.append([section_left, section_right])

	
checked = [0] * (MAX_R + 1)

for x1, x2 in segments:
	# OFFSET을 더해줍니다.
	x1, x2 = x1 + OFFSET, x2 + OFFSET
	
	# 구간을 칠해줍니다.
	# 구간 단위로 진행하는 문제이므로
	# x2에 등호가 들어가지 않음에 유의합니다.
	for i in range(x1, x2):
		checked[i] += 1

# 2번 이상 지나간 영역의 크기를 구합니다.
cnt = 0
for elem in checked:
	if elem >= 2:
		cnt += 1
print(cnt)


# ----------------------------------------- #


n = int(input())
x = []
dir = []
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)

# Please write your code here.

# x 에는 값이 저장되고 dir 에는 방향이 저장된다.
# x[i] dir[i] = 거리 방향


# 전체 리스트 생성
field = [0] * 2001 # x의 범위가 1부터 10까지이고 L 이면 -, R 이면 + 이다.
# 10 l 만 100번 나오면 어떡하지
# - 10 * 100 까지 가는거네
# offset = 1000 
# 그럼 필드도 수정해야겠네 -1000 < field < 1000
offset = 1000

# 시작지점 offset 설정

position = 0
segment_lst = []

for idx in range(n):
    distance, dirrection = x[idx], dir[idx]
    if dir[idx] == 'L':
        distance = -distance
    # 필요 없나보다
    # 필요하네
    
    # 음수로 설정하면 조금 복잡해지나? 그냥 더해버릴까
    # 아니다 어차피 더할거구나
    # 시작지점 변수 설정 해야하네

    # 시작지점은 offset 이고 dir에 따라 분기처리 해야하나보다.
    if distance < 0:
        for dots in range(position + distance, position + 1): 
            field[dots + offset] += 1
            segment_lst.append([position + distance, position + 1])

    else:
        for dots in range(position, position + distance + 1):
            field[dots + offset] += 1
            segment_lst.append([position + distance, position + 1])

    position += distance

# for start, end in segment_lst:
#     for idx in range(start, end):





count = 0
for val in field:
    if val >= 2:
        count += 1

print(count - len(segment_lst))

# # 영역의 크기 ?
# area_list = []

# # start = 0
# end = 0
# for idx in range(end + 1, len(field)):
#     if field[idx] >= 2:
#         start = idx
#         for search in range(start, len(field) - idx):
#             if field[search + 1] < 2:
#                 end = search
#                 area_list.append(end - start)
#                 break
# print(sum(area_list) - len(area_list))