```python
T = int(input())
for test_num in range(1,T+1):
    N,M = map(int,input().split())
    NL = list(map(int,input().split()))
    ML = list(map(int,input().split()))
    hap = 0
    if N ==M:
        for i in range(N):
            hap+=NL[i]*ML[i]
    elif N > M:
        # 윈도우 돌면서 확인
        
        for i in range(N-M+1):
            temp = 0
            for j in range(M):
                temp+=NL[i+j]*ML[j]
            # print(temp,hap)
            hap = max(temp,hap)
    else:
        # 윈도우 돌면서 확인
        for i in range(M-N+1):
            temp = 0
            for j in range(N):
                temp+=ML[i+j]*NL[j]
            # print(temp,hap)
            hap = max(temp,hap)
    print(f'#{test_num} {hap}')

```


```python

N,M = map(int,input().split())
L1 = list(map(int,input().split()))
L2 = list(map(int,input().split()))
L3 = L1+L2

print(* sorted(L3))

```


일단 문제들을 풀고 올렸습니다.
추가로 다른 공부들을 하고 있는지도 모르겠고 집중도 안되고 큰일입니다.