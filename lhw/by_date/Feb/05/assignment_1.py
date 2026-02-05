n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.

field = [0] * 100

for start, end in segments:
    for dots in range(start, end + 1) :
        field[dots] += 1

print(max(field))