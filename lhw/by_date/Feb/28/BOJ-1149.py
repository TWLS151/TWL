# BOJ - 1149
# RGB 거리

N = int(input())
street = [list(map(int, input().split())) for _ in range(N)]

# 1번 집은 2번과 다르고
# N 과 N-1 도 다르고
# I 는 I-1 I+1 과도 다르다.

# 모든 결과를 다 보지만, 이미 알고 있는 경우는 안본다.

r, g, b = street[0]

for idx in range(1, N):
    pr, pg, pb = street[idx]
    nr = pr + min(g, b)
    ng = pg + min(r, b)
    nb = pb + min(r, g)
    r, g, b = nr, ng, nb

print(min(r, g, b))