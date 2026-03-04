# BOJ - 9663
# N-QUEEN

N = int(input())

col = [False] * N
diag1 = [False] * (2*N)  # r + c 는 항상 같음.
diag2 = [False] * (2*N)  # r - c 도 항상 같음.

count = 0

def dfs(r):
    global count
    # 기저: r == N
    if r == N:
        count += 1
        return
    
    for c in range(N):
        if not col[c] and not diag1[r+c] and not diag2[r-c+N-1]:
            col[c] = True
            diag1[r+c] = True
            diag2[r-c+N-1] = True
            
            dfs(r+1)

            col[c] = False
            diag1[r+c] = False
            diag2[r-c+N-1] = False

    pass

dfs(0)
print(count)