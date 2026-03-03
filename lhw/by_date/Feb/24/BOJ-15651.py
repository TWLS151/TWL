# BOJ - 15651
# N과 M 3
# 백트래킹


def dfs(lst):
    global N, M

    if len(lst) == M:
        print(*lst)
        return
    
    # 반복할 것
    # N 까지의 자연수를 하나씩 선택

    for i in range(1, N+1):
        if lst:
            if lst[-1] <= i:
                lst.append(i)
                dfs(lst)
                lst.pop()
        else:
            lst.append(i)
            dfs(lst)
            lst.pop()

    pass

N, M = map(int, input().split())

lst = []
dfs(lst)



# 1부터 N 까지 자연수 중에서 M 개를 고른 수열
# 중복 가능
