x1 = [0] * 3
y1 = [0] * 3
x2 = [0] * 3
y2 = [0] * 3

x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())
x1[2], y1[2], x2[2], y2[2] = map(int, input().split())

# Please write your code here.

offset = 1000

field = [[0] * 2001 for _ in range(2001)]

for idx in range(2):
    for i in range(x1[idx], x2[idx]):
        for j in range(y1[idx], y2[idx]):
            field[i+offset][j+offset] += 1

for i in range(x1[2], x2[2]):
    for j in range(y1[2], y2[2]):
        field[i+offset][j+offset] = 0

count = 1
for i in range(2001):
    for j in range(2001):
        if field[i][j] >= 1:
            count += 1

print(count)