# SWEA - 1486
# 장훈이의 높은 선반

def findHeight(idx, cur_height):
    global min_height

    if cur_height >= min_height:
        return
    
    if idx == N:
        if cur_height >= B:
            min_height = min(cur_height, min_height)
        return
    
    findHeight(idx + 1, cur_height)
    findHeight(idx + 1, cur_height + heights[idx])




TC = int(input())

for test_case in range(1, TC+1):
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))

    # DFS 로 풀자

    min_height = float('inf')

    findHeight(0, 0)

    print(f'#{test_case} {min_height - B}')