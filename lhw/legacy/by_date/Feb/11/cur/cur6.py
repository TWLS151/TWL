# BOJ - 2630
# 색종이 만들기

# 1. base_case
# 구역 안에 다른 색이 없을 때


# 2. recurse
# 인자로 받은 배열을 순회면서 다른 색이 나오면 4 사분면으로 나눈다.
# 숫자도 센다.

def colourPaper(x, y, n):
    color = paper[x][y]
    for row in range(x, x+n):
        for col in range(y, y+n):
            if color != paper[row][col]:
                m = n//2
                colourPaper(x, y, m)
                colourPaper(x, y+m, m)
                colourPaper(x+m, y, m)
                colourPaper(x+m, y+m, m)
                return
    if color == 0:
        result[0] += 1
    else:
        result[1] += 1

N = int(input())

paper = [list(map(int, input().split())) for _ in range(N)]

result = [0, 0]
colourPaper(0, 0, N)
print(f'{result[0]} {result[1]}')