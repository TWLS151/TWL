# SWEA - 2112
# 보호 필름

import sys
sys.stdin = open('z.txt')

def check(film, D, W, K):
    if K == 1:
        return True
    
    for c in range(W):
        cnt = 1
        ok = False
        for r in range(1, D):
            if film[r][c] == film[r-1][c]:
                cnt += 1
            else:
                cnt = 1
            if cnt >= K:
                ok = True
                break
        if not ok:
            return False
    return True

def dfs(r, used):
    global best, film, D, W, K

    if used >= best:
        return
    
    if r == D:
        if check(film, D, W, K):
            best = used
        return
    
    original = film[r][:]

    dfs(r + 1, used)

    film[r] = [0] * W
    dfs(r+1, used+1)

    film[r] = [1] * W
    dfs(r+1, used+1)

    film[r] = original


T = int(input())
for tc in range(1, T+1):
    D, W, K = map(int, input().split())
    film = [list(map(int, input().split())) for _ in range(D)]

    if check(film, D, W, K):
        print(f'#{tc} 0')
        continue

    best = K
    dfs(0, 0)
    print(f'#{tc} {best}')


'''
# 푸는 내내 DFS 문제라는 생각을 한 번도 하지 못헀다.

1. 문제를 샅샅히 뒤져야한다.
 # 문제에서 K 는 1부터 시작한다고 되어있는데 K가 1이라면 약을 뿌리지 않아도 바로 통과가 가능한 상태임
 # 그럼 가지치기를 한 번 할 수 있음
 # 또한 약을 뿌리는 횟수가 K 를 넘어갈 수 없음
 # K행을 그대로 약을 뿌리면 바로 통과되기 때문

2. 백트래킹
 # 백트래킹 하는 과정에서 처음에 카피 모듈을 불러와서 딥카피로 진행헀는데 하면서도 이러면 메모리를 너무 많이 먹는게 아닌가
 # 라는 생각을 했다. 그래도 진행했는데 위의 DFS 함수 백트래킹을 보면 아주 깔끔하게 필요한 부분만 처리하는 걸 볼 수 있음

3. 카운팅 방식
 # 위 CHECK 함수의 카운팅 방식을 생각하지 못한 건 아니지만 조금 더 클레버하게 할 순 없을까 고민하다가
 # 결국 이상한 방법으로 진행헀다.
 # 그냥 일단 하자.

 
 ## DFS 문제의 힌트 ##
 1. 요소를 하나씩 순서대로 결정하는 구조인가?
 2. 각 단계에서 선택지가 여러개인가?
 3. 최소 / 최대 조건이 있는가?
 4. 가지치기가 가능한가?

 해당 문제는 '행을 하나씩 보면서 어떻게 처리할지 선택하고 최소 변경 횟수를 찾는 문제'
 전형적인 백트래킹 DFS 라고 한다.

'''