# BOJ - 12100
# 2048 Easy

# import sys
# sys.stdin = open('input.txt')


def compress_and_merge(line):

    N = len(line)
    arr = [x for x in line if x != 0]
    merged = []
    i = 0
    while i < len(arr):
        if i + 1 < len(arr) and arr[i] == arr[i+1]:
            merged.append(arr[i] * 2)
            i += 2
        else: 
            merged.append(arr[i])
            i += 1
    merged += [0] * (N - len(merged))
    return merged

def move_left(board):
    N = len(board)
    new_board = []
    for r in range(N):
        new_board.append(compress_and_merge(board[r]))
    return new_board

def move_right(board):
    N = len(board)
    new_board = []
    for r in range(N):
        rev = list(reversed(board[r]))
        merged = compress_and_merge(rev)
        new_board.append(list(reversed(merged)))
    return new_board

def move_up(board):
    N = len(board)
    new = [row[:] for row in board]
    for c in range(N):
        col = [board[r][c] for r in range(N)]
        merged = compress_and_merge(col)
        for r in range(N):
            new[r][c] = merged[r]
    return new

def move_down(board):
    N = len(board)
    new = [row[:] for row in board]
    for c in range(N):
        col = [board[r][c] for r in range(N)]
        col.reverse()
        merged = compress_and_merge(col)
        merged.reverse()
        for r in range(N):
            new[r][c] = merged[r]
    return new

def get_max_tile(board):
    return max(map(max, board))

def dfs(board, depth):
    if depth == 0:
        return get_max_tile(board)
    
    best = 0

    for nxt in (move_left(board), move_right(board), move_up(board), move_down(board)):
        best = max(best, dfs(nxt, depth - 1))
    
    return best

def main():
    N = int(input().strip())
    board = [list(map(int, input().split())) for _ in range(N)]
    print(dfs(board, 5))

if __name__ == "__main__":
    main()



# 겹치면 합쳐진다.
# 한 번의 이동에서는 한 번만 합쳐진다.
# 같은 수가 세 개면 벽에 가까운 두개가 먼저 합쳐진다.
# 5번까지 이동해서 가장 큰 블록의 값을 구해라
