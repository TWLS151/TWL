n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x, y = zip(*points)
x, y = list(x), list(y)

# Please write your code here.

offset = 100

matrix = [[0] * 201 for _ in range(201)]

for idx in range(n):
    for i in range(x[idx], x[idx] + 8):
        for j in range(y[idx], y[idx] + 8):
            matrix[i + offset][j + offset] += 1

count = 0
for i in range(201):
    for j in range(201):
        if matrix[i][j] != 0:
            count += 1
    
print(count)


