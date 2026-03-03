# 포탈 풀이!!


소신 발언! 문제 이해하는데에 좀 걸렸고
정작 풀고 디버깅하는데에는 20분 정도 걸렸습니다.
이해를 돕는 그림 같은게 있으면 좋겠다고 생각했습니다.
그리고, 지금은 그냥 구현의 방식으로만 문제를 풀었지만,
```구현``` 방식 이외에 다른 우아한 방식이 있을 것이라고 생각이 됩니다.

그런 방법을 찾게 된다면 한번 말씀드리도록 하겠습니다.



```python
T = int(input())
for test_num in range(1,T+1):
    roomnum = int(input()) #방 번호 마지막
    rooms = list(map(int,input().split()))
    #방 별 포탈 2개
    # 젤먼저 들어오면 걍 바로 오른쪽으로 감
    # 짝수번째로 들어오면 왼쪽 어딘가로 가는 포탈을 탐
    # 단 1번방 (2번째 인덱스의 방은 걍 무조건 다음 방으로감 감)
    roomstats = [0]*roomnum
    # print(roomstats)
    curr = 0
    moves = 0
    while curr != roomnum-1:
    # for _ in range(12):
        # print(f'방문한 방은 {curr} 이며 방상태는 {roomstats[curr]}',end = '')
        if curr == 0:
            roomstats[curr] =1
            curr+=1
            moves+=1 
            
        elif roomstats[curr] == 0: #맨 처음에 들어왔고 바로 왼쪽으로 가는 포탈을 타야함
            roomstats[curr] = 1
            curr = rooms[curr]-1 # 이 방의 포탈이 나를 이끄는 곳으로 가야한다
            moves+=1
            #그리고 룸 상태를 방문 상태로 바꾼다
            
           
        else: # 두번재 들어왔을떄 부터는 걍 오른쪽으로 쭉 간다.
            curr += 1
            moves+=1
        
        # print(f'이제 방 {curr}로 갑니다.')



    print(f'#{test_num} {moves}')
```



근데? 제가 방금 풀어버렸습니다.

```python 
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    portals = list(map(int, input().split()))
    answer = N-1 + (N-2)
    # 포탈 수 + 원래 이동해야 하는 수는 이미 정해져 있음으로 초기 값으로 설정
    
    # 포탈들을 쭉 돌면서, 이 포탈을 부득이하게 지나면서 추가로 이동해야 하는 횟수를 계산하여 더해줍니다.
    # 결국 이 자리까지 와야하기 때문에 (내 자리 값 - 이동하게 되는 값)을 더해주었습니다.
    for i in range(1,N-1):
        answer = answer + (i+1 - (portals[i]))
    print(f'#{tc} {answer}')
```