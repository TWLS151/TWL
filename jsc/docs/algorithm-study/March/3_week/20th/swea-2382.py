# SWEA 2382 미생물 격리

def solve():
    
    for _ in range(M):
        next_step = {}
        
        for (r, c), info in clusters.items():
            cnt, dr, _ = info
            
            nr, nc = r + dr_map[dr], c + dc_map[dr]
            
            if nr == 0 or nr == N-1 or nc == 0 or nc == N-1:
                cnt //= 2
                dr = reverse_dr(dr) 
                if cnt == 0: continue 
            
            if (nr, nc) not in next_step:
                next_step[(nr, nc)] = [cnt, dr, cnt] 
            else:
                prev_cnt, prev_dr, max_cnt = next_step[(nr, nc)]
                if cnt > max_cnt:
                    next_step[(nr, nc)] = [prev_cnt + cnt, dr, cnt]
                else:
                    next_step[(nr, nc)][0] += cnt
        
        clusters = next_step 
