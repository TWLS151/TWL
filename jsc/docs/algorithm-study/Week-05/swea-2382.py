import sys

def solve():
    T = int(input())
    
    # 1: 상, 2: 하, 3: 좌, 4: 우 (0번 인덱스는 더미)
    dr = [0, -1, 1, 0, 0]
    dc = [0, 0, 0, -1, 1]
    
    # 반대 방향 매핑 (1<->2, 3<->4)
    rev_d = [0, 2, 1, 4, 3] 

    for tc in range(1, T + 1):
        # N: 셀의 개수, M: 격리 시간, K: 미생물 군집의 개수
        N, M, K = map(int, input().split())
        
        # 미생물 군집 정보 리스트: (r, c, n, d)
        microbes = []
        for _ in range(K):
            r, c, n, d = map(int, input().split())
            microbes.append((r, c, n, d))
            
        # M시간 동안 시뮬레이션 진행
        for _ in range(M):
            # 다음 위치별로 미생물 군집을 모아둘 딕셔너리
            # key: (r, c), value: [(미생물 수, 방향), ...]
            cell_dict = {}
            
            # 1. 미생물 이동 로직
            for r, c, n, d in microbes:
                nr = r + dr[d]
                nc = c + dc[d]
                
                # 약품 구역(가장자리)에 도달한 경우
                if nr == 0 or nr == N - 1 or nc == 0 or nc == N - 1:
                    n //= 2  # 미생물 수 반으로 감소
                    d = rev_d[d]  # 방향 반대로 전환
                    if n == 0:  # 미생물 수가 0이 되면 소멸
                        continue
                
                if (nr, nc) not in cell_dict:
                    cell_dict[(nr, nc)] = []
                cell_dict[(nr, nc)].append((n, d))
                
            # 2. 군집 병합 로직 및 다음 상태 준비
            next_microbes = []
            for (r, c), group_list in cell_dict.items():
                if len(group_list) == 1:
                    # 해당 칸에 군집이 1개뿐이면 그대로 추가
                    next_microbes.append((r, c, group_list[0][0], group_list[0][1]))
                else:
                    # 여러 군집이 모였을 경우 병합
                    total_n = 0
                    max_n = 0
                    max_d = 0
                    
                    for n, d in group_list:
                        total_n += n
                        # 가장 미생물 수가 많은 군집의 방향으로 설정
                        if n > max_n:
                            max_n = n
                            max_d = d
                            
                    next_microbes.append((r, c, total_n, max_d))
            
            # 다음 시간대를 위해 업데이트
            microbes = next_microbes
            
        # M시간 후 남아있는 총 미생물 수 계산
        total_microbes = sum(m[2] for m in microbes)
        print(f"#{tc} {total_microbes}")

if __name__ == "__main__":
    solve()