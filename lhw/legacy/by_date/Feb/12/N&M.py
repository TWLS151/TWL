# BOJ - 15649
# N과 M

# 1 부터 N 까지 자연수 중에서 중복 없이 M 개를 고른 수열
# 중복 없다 > 방문 처리
# 무향성

# 할 일이 뭔데?
# 고른 적 없는 수 고르기
# 그럼 뭐가 있어야하지?
# 숫자 목록이랑 고른 적 있는지 봐야지


def arr(lst, m):

    if len(result) == m:
        print(*result)
        return

    for i in lst:
        if not visited[i]:
            # result.append(i)
            visited[i] = True
            result.append(i)
            arr(lst, m)
            visited[i] = False
            result.pop()


n, m = map(int, input().split())

lst = [i for i in range(1, n+1)]
visited = [False for i in range(n+1)]

result = []

arr(lst, m)