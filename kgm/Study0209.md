# 2026.02.09 스터디
## swea 4613번 러시아 국기 같은 깃발

- 2시간 동안 풀었지만 결국 제미나이 도움을 받음
- 생각 : 첫번째와 끝은 무조건 흰색과 빨간색이니 그 사이에서 파란색의 시작 위치와 범위를 옮기며 가능한 경우를 모두 구한 뒤 그 중 최소의 횟수를 찾자!

초기 코드
``` python
T = int(input())

for tc in range(1,1+T):
    N, M = map(int, input().split())
    color = [list(input()) for i in range(N)]
    
    w_list=[]
    b_list=[]
    r_list=[]

    for i in range (N):
        w_list.append(color[i].count('W'))
        b_list.append(color[i].count('B'))
        r_list.append(color[i].count('R'))
    
    result=[]

    for i in range(1,N-1): 
        for z in range(i+1, N-1):
            temp=0
            if i ==1 and z == N-2 :      # 안쪽이 모두 파란색일 
                for q in range(1,N-1):
                    temp += M - b_list[q]
                # print(f'blue {temp}')
                result.append(temp)
            elif z == N-2 :              # 마지막이 파란색일 때
                for white in range(1,i):
                    temp += M - w_list[white]
                for blue in range(i,z):
                    temp += M - b_list[blue]
                # print(f'white {temp}')
                result.append(temp) 
            elif i == 1:                #시작이 파란색일 때                    
                for red in range (z, N-1):
                    temp += M - r_list[red]
                for blue in range(i,z):
                    temp += M - b_list[blue]
                result.append(temp)
                # print(f'red {temp}')
            else:
                for white in range(1,i):
                    temp += M - w_list[white]
                for blue in range(i,z+1):
                    temp += M - b_list[blue]        
                for red in range (z+1,N-1):
                    temp += M - r_list[red]
                result.append(temp)
    
    num=min(result) + 2*M - w_list[0] - r_list[N-1]
    print(f'#{tc} {num}')

```
이 코드의 문제점 -> 범위를 1 ~ N-2로 나누어 헷갈리게 함, if와 elif 문으로 경우를 계속 나누어 복잡하게 만듦.

이에 1시간 정도 고민 한 후에 새로 짜기로 생각하고 3중 for문을 구성

새로운 코드
``` python
T = int(input())

for tc in range(1,1+T):
    N, M = map(int, input().split())
    color = [list(input()) for i in range(N)]
    
    w_list=[]
    b_list=[]
    r_list=[]

    for i in range (N):
        w_list.append(color[i].count('W'))
        b_list.append(color[i].count('B'))
        r_list.append(color[i].count('R'))
    
    result=[]

    for i in range(0,N-2):
        for z in range(i+1,N-1):
            temp = 0
            for white in range(0,i+1):
                temp += M - w_list[white]    
            for blue in range(i+1,z+1):
                temp += M - b_list[blue]
            for red in range(z+1, N):
                temp += M - r_list[red]
        result.append(temp)             # 이부분을 한번 tap 해야함
            # result.append(temp)
    num = min(result)
    print(f'#{tc} {num}')
```
이 코드는 3중 for문을 돌린 후에 for문으로 범위 안에서 계산을 진행함. 해당 코드의 result.append 부분이 for z in range(i+1,N-1) 바깥의 범위에 있어서 문제가 발생했음.

## 현재 나의 문제점
- 당근 분배 문제와 러시아 국기 같은 깃발 문제는 공통적으로 균등하게 나누는 것을 목표로 하고 있음. 이러한 문제의 경우 범위를 정하는 것이 가림막을 기준으로 해야하지만 나는 지금 범위를 정하고 거기에 맞추려고 함. 이로 인해서 if문이나 예외 처리 남용, 또한 범위를 계속해서 쪼개다 보니 인덱싱을 어디로 할지 모름
- 완전 탐색과 같은 문제에 많이 약함.