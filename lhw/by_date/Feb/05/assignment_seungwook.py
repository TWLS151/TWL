# 1

# n = int(input())
# x = []
# dir = []
# for _ in range(n):
#     xi, di = input().split()
#     x.append(int(xi))
#     dir.append(di)

# move_list = [0] * 1000
# pos = 500

# for i in range(n):

#     # 거리와 방향
#     step, direction = x[i], dir[i]

#     if direction == "R":
#         # 오른쪽으로 간다. 0 -> 3 [0, 3)
#         for j in range(pos, pos + step):
#             move_list[j] += 1
#         pos += step

#     else:
#         # 왼쪽으로 간다. 5 -> 2 5,4 4,3 3,2 [4, 2]
#         for k in range(pos - 1, pos - step - 1, -1):
#             move_list[k] += 1
#         pos -= step
# cnt = 0
# for el in move_list:
#     if el >= 2:
#         cnt += 1
# print(cnt)


# 2 -------------------------

n = int(input())

pos = 0
events = {}

min_pos = 0
max_pos = 0

for _ in range(n):
    step_s, d = input().split()
    step = int(step_s)

    if d == "R":
        a = pos
        b = pos + step # 지나간 구간: [pos, pos + step)
        pos = b
    else:
        a = pos - step
        b = pos # 지나간 구간: [pos - step, pos)
        pos = a 

    # 차분 기록
    events[a] = events.get(a, 0) + 1
    events[b] = events.get(b, 0) - 1

    min_pos = min(min_pos, a, b)
    max_pos = max(max_pos, a, b)
    # 음수 좌표 방지용 OFFSET
    OFFSET = -min_pos
    size = (max_pos - min_pos) + 2

    diff = [0] * size
    for p, v in events.items():
        diff[p + OFFSET] += v

# 누적합으로 각 구간(i~i+1)의 횟수(cur) 복원
cur = 0
cnt = 0
for i in range(size - 1):
    cur += diff[i]
    if cur >= 2:
        cnt += 1
print(cnt)