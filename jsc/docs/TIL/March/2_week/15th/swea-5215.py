import sys

sys.stdin = open('swea-5215.txt')

def dfs(idx, current_score, current_kcal):
    global max_score
    
    # 1. 가지치기: 이미 제한 칼로리를 넘었다면 중단
    if current_kcal > L:
        return

    # 2. 기저 조건: 모든 재료를 다 확인했을 때
    if idx == N:
        if current_score > max_score:
            max_score = current_score
        return

    # 3. 현재 재료(idx)를 사용하는 경우
    dfs(idx + 1, current_score + scores[idx], current_kcal + calories[idx])
    
    # 4. 현재 재료(idx)를 사용하지 않는 경우
    dfs(idx + 1, current_score, current_kcal)

T = int(input())

for tc in range(1, T + 1):
    N, L = map(int, input().split())
    rough_data = [list(map(int, input().split())) for _ in range(N)]

    scores = [x[0] for x in rough_data]
    calories = [x[1] for x in rough_data]

    max_score = 0
    # 시작 인덱스 0, 현재 점수 0, 현재 칼로리 0으로 시작
    dfs(0, 0, 0)

    print(f"#{tc} {max_score}")