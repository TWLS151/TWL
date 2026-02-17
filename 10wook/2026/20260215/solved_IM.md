숫자 배열 회전
```python
T= int(input())
for test_num in range(1,T+1):
    N= int(input())
    origin = []
    for _ in range(N):
        origin.append(list(map(int,input().split())))
    list90 = [[0]*N for _ in range(N)]
    list180 = [[0]*N for _ in range(N)]
    list270 = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            list90[j][N-1-i] = origin[i][j]
    for i in range(N):
        for j in range(N):
            list180[j][N-1-i] = list90[i][j]        
    for i in range(N):
        for j in range(N):
            list270[j][N-1-i] = list180[i][j]
    print(f'#{test_num}') 
    for i in range(N):
        print(*list90[i], ' ',*list180[i],' ' ,*list270[i], sep = '')
```

불끄기 뭐시기
```python
def turn(num):
    if num ==0:
        return 1
    else:
        return 0
N = int(input())
switchs = [-1]+list(map(int,input().split()))
M = int(input())
for _ in range(M):
    sex,num = map(int,input().split())
    if sex == 1:
        for i in range(num,N+1,num):
            switchs[i] = turn(switchs[i])
    else:
        check = 1
        switchs[num] = turn(switchs[num])
        while num +check <=N and num-check>=1:
            if switchs[num-check]!=switchs[num+check]:
                break
            else:
                switchs[num-check] = turn(switchs[num-check])
                switchs[num+check] = turn(switchs[num+check])
                check+=1
                
for i in range(1,N+1):
    if i%20==0:
        print(switchs[i])
    else:
        print(switchs[i],end=' ')
```