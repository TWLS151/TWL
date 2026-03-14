# BOJ-1149
# RGB 거리
# DP


N = int(input())

r, g, b = map(int, input().split())

for _ in range(2, N+1):
    cr, cg, cb = map(int, input().split())
    nr = cr + min(g, b)
    ng = cg + min(r, b)
    nb = cb + min(r, g)
    r, g, b = nr, ng, nb

print(min(r, g, b))