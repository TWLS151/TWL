import sys
from collections import deque
sys.stdin = open('swea_5099_피자 굽기.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    cheese_lst = []
    lst_ = list(map(int, input().split()))
    for i in range(1, len(lst_) + 1):
        cheese_lst.append([i, lst_[i-1]])
    # 이건 AI한테 물어봐서 인덱스랑 값을 동시에 저장하는 방법을 배웠네요...
    # -> cheese_lst = [[i, v] for i, v in enumerate(map(int, input().split()), start=1)] 
    oven = [] # 오븐 리스트
    for i in range(N):
        oven.append(cheese_lst.pop(0)) # 1, 2, 3, .....번 피자의 인덱스와 치즈 양을 오븐에 순서대로 추가
    while(len(oven)) > 1:
        num , cheese = oven.pop(0) # 꺼내서 확인하는 과정
        cheese //= 2 # 치즈 양 절반으로
        if cheese != 0: # 치즈가 남아있으면
            oven.append([num, cheese]) # 다시 오븐에 넣기
        elif cheese_lst: # 치즈 목록에 남아있는 것이 있으면(True는 값이 존재한다는 의미)
            oven.append(cheese_lst.pop(0)) # 다시 넣기
    print(f'#{tc} {oven[0][0]}')

##########################################################################################

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    cheese_lst = deque([i + 1, v] for i, v in enumerate(map(int, input().split())))
    
    oven = deque()
    for i in range(N):
        oven.append(cheese_lst.popleft())
    while len(oven) > 1:
        num, cheese = oven.popleft()
        cheese //= 2
        if cheese!= 0:
            oven.append([num, cheese])
        elif cheese_lst:
            oven.append(cheese_lst.popleft())
    print(f'#{tc} {oven[0][0]}')