import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

def tsar_bomba(arr, N, M):
    
    total_power = 0
    
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
        
    for r in range(N):
        for c in range(M):
            
            power = arr[r][c]
            
            for d in range(4):
                for p in range(1, arr[r][c]+1):
                
                    nr = r + dr[d]*p
                    nc = c + dc[d]*p

                    if 0 <= nr < N and 0 <= nc < M:
                        power += arr[nr][nc]
            
            if total_power < power:
                total_power = power
                
    return total_power

for tc in range(1, T+1):
    
    N, M = map(int, input().split())
    
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    result = tsar_bomba(arr, N, M)
    
    print(f"#{tc} {result}")