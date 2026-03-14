# BOJ - 15650
# N과 M (2)


def cob(start):

    if len(result) == m:
        print(*result)
        return
    
    for i in range(start, n+1):
        result.append(i)
        cob(i + 1)
        result.pop()

# def arr(lst, m):

#     if len(result) == m:
#         print(*result)
#         return

#     for i in lst:
#         if not visited[i]:
#             # result.append(i)
#             visited[i] = True
#             result.append(i)
#             # print(f'추가하고 바로 출력 {result}')

#             if i >= max(result):
#                 arr(lst, m)

            
#             visited[i] = False

#             result.pop()
#             # print(f'팝 하고 출력 {result}')

n, m = map(int, input().split())

lst = [i for i in range(1, n+1)]
# visited = [False for i in range(n+1)]

result = []

# arr(lst, m)
cob(1)