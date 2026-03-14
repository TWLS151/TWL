# BOJ - 9663
# N - QUEEN
# 백트래킹


def queen(r):
    global N, col

    if r == N:
        return

    for c in range(N):
        if not col[c]:
            col[c] = True
            queen(r+1)
            col[c] = False


    pass

N = int(input())
col = [False]*N
