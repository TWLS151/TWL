## offset 개념에 대해 알았따.
# 범위가 주어지지 않으면 내가 찾으면 되잖아?

line_num = int(input())

range_list = [list(map(int, input().split())) for _ in range(line_num)]

offset = min(range_list, key= lambda x: x[0])

inset = max(range_list, key= lambda x: x[1])

length = [0] * (inset[1] - offset[0])

for start, end in range_list:
    for idx in range(start, end):
        length[idx + abs(offset[0])] += 1

print(max(length))



## 강사님 풀이

# OFFSET = 100

# n = int(input())
# segments = [tuple(map(int, input().split())) for _ in range(n)]

# counts = [0] * 201

# for s, e in segments:
#     for i in range(s, e):
#         counts[i + OFFSET] += 1

# print(max(counts))



