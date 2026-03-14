# SWEA - 1267
# 작업순서

# import sys
# sys.stdin = open('sequence.txt')

def findSame(node):

    visited[node] = True

    for child in adj_info[node]:
        if not visited[child]:
            findSame(child)

    order.insert(0, node)


for test_case in range(1, 11):
    V, E = map(int, input().split())
    edge_info = list(map(int, input().split()))
    visited = [False for _ in range(V+1)]

    adj_info = [[] for _ in range(V+1)]
    for i in range(E):
        p, c = edge_info[i*2], edge_info[i*2 +1]

        adj_info[p].append(c)

    order = []

    for i in range(1, V+1):
        if not visited[i]:
            findSame(i)

    print(f'#{test_case}', *order)






# def dfs(node):
#     # 방문처리 하고
#     visited[node] = True
#     # 자식으로 들어가봐야하는데

#     # 이 반복문이 핵심인게 자동으로 종료조건을 설정해준다.
#     # tree[node]가 비어있으면 어떻게 하나 생각하고 있었는데
#     # 이렇게 반복문으로 해버리면 리스트가 비어있는 경우 실행되지 않음
#     # => 자동으로 종료된다.
#     for child in tree[node]:
#         # child가 있어도 방문했던 곳이면 자동으로 걸러준다.
#         if not visited[child]:
#             dfs(child)
#     # 부모부터 출력을 해야하는 문제인데 그냥 append를 사용하면 마지막으로 작업이 끝난 자식부터 출력되기 때문에
#     # insert 사용.
#     ## append 로 집어넣고 마지막에 reverse 하는 방법도 있음
#     result.insert(0, node)

# TC = 10
# for test_case in range(1, 11):
#     V, E = map(int, input().split())
#     edge = list(map(int, input().split()))
#     visited = [False for _ in range(V+1)]

#     tree = [[] for _ in range(V+1)]
#     for i in range(E):
#         p, c = edge[i*2], edge[i*2 + 1]
#         # 유향이니까 부모쪽에 자식만 표시한다.
#         tree[p].append(c)
#     # print(tree)
#         # 이러면 인접 리스트는 만들었는데..

#     result = []
#     # 방문하지 않았던 곳만 순회
#     for idx in range(1, len(tree)):
#         if not visited[idx]:
#             dfs(idx)

#     print(f'#{test_case}', *result)