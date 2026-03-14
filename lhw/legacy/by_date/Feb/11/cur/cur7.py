# BOJ - 1992
# 쿼드트리

# 색종이랑 비슷함

def quad(x, y, n):
    num = video[x][y]

    for row in range(x, x+n):
        for col in range(y, y+n):
            if num != video[row][col]:
                m = n//2
                return "(" + \
                quad(x, y, m) + \
                quad(x, y+m, m) + \
                quad(x+m, y, m) + \
                quad(x+m, y+m, m) + \
                ")"
    return num
    pass

N = int(input())

video = [[i for i in input()] for _ in range(N)]

result = []

result = quad(0,0,N)

print(result)

