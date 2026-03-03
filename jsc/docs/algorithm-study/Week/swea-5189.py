import sys


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    
    targets = [i for i in range(1, N)]
    all_paths = []
    visited = [False] * len(targets)
    
    def get_perm(current_path):
        if len(current_path) == len(targets):
            return
        
        for i in range(len(targets)):
            if not visited[i]:
                visited[i] = True
                current_path.append(targets[i])
                get_perm(current_path)
                current_path.pop()
                visited[i] = False

    get_perm([])
    
    
    min_battery = float('inf')
    
    for path in all_paths:
        total = 0
        curr = 0
        
        for next_node in path:
            total += board[curr][next_node]
            curr = next_node      

        total += board[curr][0]

        if total < min_battery:
            min_battery = total
    
    print(f"#{tc} {min_battery}")

solve()