n = int(input())
x1, y1, x2, y2 = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a)
    y1.append(b)
    x2.append(c)
    y2.append(d)

# Please write your code here.

# (x1, y1) (x2, y2)

# # 넓이? 점의 오른쪽 위까지니까 넓이하면 x2 + 1, y2 + 1인듯?
# # 해보자

# for idx in range(n):
#     area = (x2[idx] + 1 - x1[idx]) * (y2[idx] + 1 - y1[idx])


# 아 배열은 싫은데..

matrix = [[0] * 201 for _ in range(201)]
count = 0

for idx in range(n):
    for i in range(x1[idx], x2[idx] - 1):
        for j in range(y1[idx], y2[idx] - 1):
            matrix[i][j] = 1
            count += 1
            
print(count)