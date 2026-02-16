N,K = map(int,input().split())
L = list(map(int,input().split()))
prefixed_sum = [0]
for i in range(N):
    prefixed_sum.append(prefixed_sum[i]+L[i])
answer =  - float('inf')
for i in range(0,N+1-K):
    answer = max(prefixed_sum[i+K]-prefixed_sum[i],answer)
    
print(answer)