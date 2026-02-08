T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    word = [input() for _ in range(N)]
    result = None
    # 가로줄에서 구하는 과정
    for r in range(N):
        for c in range(N - M + 1):     
            if word[r][c : c + M] == word[r][c : c + M][::-1]:
                result = word[r][c : c + M]
    if not result: # 가로에서 못 찾았을 경우에만 진행
        # 세로에서 구하는 과정
        v_word = list(zip(*word))
        # zip 사용해서 돌린 다음 가로줄이랑 똑같이 검사
        for r in range(N):
            for c in range(N - M + 1):
                if v_word[r][c : c + M] == v_word[r][c : c + M][::-1]:
                    result = ''.join(v_word[r][c : c + M]) 
                    # 여기 result 구현을 좀 더 깔끔하게 할 수 있는지 모르겠음.
                
    print(f'#{tc} {result}')








