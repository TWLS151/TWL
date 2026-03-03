# ABC 281 - A
# Count Down

N = int(input())
for i in range(N, -1, -1):
    print(i)

# N 부터 카운트 다운을 출력하는 문제
# 처음에
# print(i for i in range(N, -1, -1))
# 컴프리헨션을 시도헀는데
# 이렇게 해도 제너레이터가 출력되는 걸 보고 살짝 당황
# 그래서 그냥 풀어서 출력했습니당.

# 지피티한테 물어보니까
# print(*range(N, -1, -1), sep='\n')
# 이렇게 출력해야 한다네용~