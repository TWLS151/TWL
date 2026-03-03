x1, y1, x2, y2 = [0] * 2, [0] * 2, [0] * 2, [0] * 2
x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())

# Please write your code here.

# 처음 사갹형은 1
# 두번째 사각형은 0
# 그럼 1 남은 것들 중에 min x ~ max x, min y ~ max y

matrix = [[0] * 2001 for _ in range(2001)]

for idx in range(1):
    for i in range(x1[idx], x2[idx]):
        for j in range(y1[idx], y2[idx]):
            matrix[i+1000][j+1000] = 1

for idx in range(1, 2):
    for i in range(x1[idx], x2[idx]):
        for j in range(y1[idx], y2[idx]):
            matrix[i+1000][j+1000] = 0

# 남은 1들 좌표 뽑기
xa, ya = 0, 0
xb, yb = 0, 0
for i in range(2001):
    for j in range(2001):
        if matrix[i][j] == 1:
            if xa < i :
                xa = i
            if ya < j :
                ya = j
            if xb > i :
                xb = i
            if yb > j:
                yb = j

print((xa - xb) * (ya - yb))






# x1, y1, x2, y2 = [0] * 2, [0] * 2, [0] * 2, [0] * 2
# x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
# x1[1], y1[1], x2[1], y2[1] = map(int, input().split())

# # Please write your code here.

# # 처음 사갹형은 1
# # 두번째 사각형은 0
# # 그럼 1 남은 것들 중에 min x ~ max x, min y ~ max y


# (x1[0], y1[0]), (x2[0], y2[0])
# (x1[1], y1[1]), (x2[1], y2[1])

# if x1[0] < x1[1]:
#     min_x = x1[0]
# else:
#     min_x = x1[1]

# if y1[0] < y1[1]:
#     min_y = y1[0]
# else:
#     min_y = y1[1]

# if x2[0] < x2[1]:
#     max_x = x2[1]
# else:
#     max_x = x2[0]

# if y2[0] < y2[1]:
#     max_y = y2[1]
# else:
#     max_y = y2[0]

# x_diff, y_diff = max_x - min_x, max_y - min_y

# offset_x, offset_y = min_x, min_y

# matrix = [[0] * (max_x) for _ in range(max_y)]

# # print(matrix)

# for i in range(x1[0], x2[0]):
#     for j in range(y1[0], y2[0]):
#         matrix[i+offset_x][j+offset_y] = 1

# for i in range(x2[0], x2[1]):
#     for j in range(y2[0], y2[1]):
#         matrix[i+offset_x][j+offset_y] = 0

# last_minx, last_miny = 0, 0
# last_maxx, last_maxy = max_x + offset_x, max_y + offset_y
# for i in range(max_x + offset_x):
#     for j in range(max_y + offset_y):
#         if matrix[i][j] == 1:
#             if last_minx > i:
#                 last_minx = i
#             if last_maxx < i:
#                 last_maxx = i
#             if last_miny > j:
#                 last_miny = j
#             if last_maxy < j:
#                 last_maxy < j

# print((last_maxx - last_minx) * (last_maxy - last_miny))
            






# offset = 

# matrix = [[0] * x2 for _ in range(col)]

# for i in range()



# matrix = [[0] * 2001 for _ in range(2001)]

# for idx in range(1):
#     for i in range(x1[idx], x2[idx]):
#         for j in range(y1[idx], y2[idx]):
#             matrix[i+1000][j+1000] = 1

# for idx in range(1, 2):
#     for i in range(x1[idx], x2[idx]):
#         for j in range(y1[idx], y2[idx]):
#             matrix[i+1000][j+1000] = 0

# # 남은 1들 좌표 뽑기
# max_x, max_y = 0, 0
# min_x, min_y = 2000, 2000

# for i in range(2001):
#     for j in range(2001):
#         if matrix[i][j] == 1:
#             if max_x < i:
#                 max_x = i
#             if max_y < j:
#                 max_y = j
#             if min_x > i:
#                 min_x = i
#             if min_y > j:
#                 min_y = j    

# if min_x >= max_x or min_y >= max_y:
#     print(0)
# else:
#     print((max_x - min_x + 1) * (max_y - min_y + 1))