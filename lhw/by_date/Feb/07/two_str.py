# SWEA - 1959
# 두개의 숫자열

import sys
sys.stdin = open('two_str.txt')

# 숫자열 두개 (길이 N, M)
# 서로 마주보는 위치를 바꿀 수 있다.
# 더 긴 쪽의 양 끝을 벗어날 수는 없다.
# 마주보는 숫자들을 곱한 뒤 모두 더할 때 최댓값을 구해라
# 3 <= N, M <= 20

# 슬라이딩 윈도우
# 브루트포스

TC = int(input())

for test_case in range(1, TC+1):
    pass
    N, M = map(int, input().split())
    first = list(map(int, input().split()))
    second = list(map(int, input().split()))

    # 순서 바꿔줘야겠다.
    if N > M:
        N, M = M, N
        first, second = second, first

    max_mul = 0
    
    #### 반복문 순서 주의 ####
    # 하나씩 밀어내면서 해야하니까
    # 그리고 N - M 지점까지 보기 위해 + 1
    for start in range(M - N + 1): 
        mul = 0
        for idx in range(N):
            mul += first[idx] * second[start + idx]
            
        if max_mul < mul:
            max_mul = mul

    print(f'#{test_case} {max_mul}')