import sys

sys.stdin = open('swea_11315_오목 판정.txt')

def omog():
    N = int(input())
    board = [input() for _ in range(N)]
    dr = [-1, 1, 0, 0, -1, -1, 1, 1]
    dc = [0, 0, -1, 1, -1, 1, -1, 1] # 8방향 지정
    
    for r in range(N):
        for c in range(N):
            if board[r][c] == 'o':
                for i in range(8): # 방향 돌기           
                    cnt = 1 
                    for j in range(1, 5): # 어차피 5개인지만 확인하면 되므로 범위 축소
                        nr = r + j * dr[i]
                        nc = c + j * dc[i]
                        if 0 <= nr < N and 0 <= nc < N and board[nr][nc] =='o':
                            cnt += 1 # 벽에 안 박고 'o'를 만나면 계속 탐색
                        else: # 그 외의 경우는 모두 캇!
                            break
                    if cnt == 5: # 5개 되는 순간 YES로 바꾸기
                        return 'YES'
                        
           
    return 'NO' # 못 찾았으면 혼나야겠제


T = int(input())
for tc in range(1, T + 1):
                    
    print(f'#{tc} {omog()}')