# BOJ-9663
# N-QUEEN


N = int(input())

count = 0

col = [-1] * N

def pos(r):
    for i in range(r):

        if col[i] == col[r]:
            return False
        
        if abs(col[r] - col[i]) == r - i:
            return False
    return True

def dfs(r):
    global count

    if r == N:
        count += 1
        return
    
    for c in range(N):
        col[r] = c
        if pos(r):
            dfs(r+1)

dfs(0)
print(count)

# ------ 최적화 ------ #

N = int(input())

count = 0

col = [False] * N
diag1 = [False] * (2*N)
diag2 = [False] * (2*N)

def dfs(r):
    global count

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



dfs(0)
print(count)