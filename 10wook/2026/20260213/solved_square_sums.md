```python

N = int(input())
# DP = []

# answer = 0
# while N > 0:
#     cnt = 0
#     while N > cnt*cnt:
#         cnt +=1
#         if len(DP) < cnt:
#             DP.append(cnt**2)
#         print(DP, N,cnt)
#     if N == DP[cnt-1]:
#         N = 0
#     else:
#         N = N - DP[cnt-2]
#     answer+=1
#     print(N,DP)
# print(answer)


#새로운 접근법이 필요하다는 것을 알게 되었습니다
# 1. 여기서 점프해서 가는 경우를 찾아봐야하고,,,, 이 전 숫자까지 확인 할 것.
# 2. 지금 부터 나 까지 1,4,9,16 ... 전 숫자 +1 중에 뭐가 제일 적은지 확인하고 추가할것

import math
DP = list(range(N+1))
for i in range(1, 1+N):
    for j in range(1, int(math.sqrt(i)) + 1):
        DP[i] = min(DP[i], DP[i - j*j] + 1)
print(DP[N])

```


일단 답은 냈지만 시간 초과가 너무 많이 나서 고민을 좀 해봐야할듯 합니다.