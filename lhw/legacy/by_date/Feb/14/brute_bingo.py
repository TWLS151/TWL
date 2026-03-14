# BOJ - 2578
# 빙고

import sys
sys.stdin = open('z.txt')

# 매트릭스 받고
# 사회자 숫자 받고
# 숫자 순회하면서
# 하나씩 지우고 지운 매트릭스 함수에 넣어서 빙고 판단
# 델타 있어야하겠고
# 반환값이 트루가 되면 그때 매트릭스 상 숫자 출력

# 숫자열로 받을 필요는 없네
board = [input().split() for _ in range(5)]
# 배열로 받을 필요는 없다.
nums = []
for _ in range(5):
    for i in input().split():
        nums.append(i)
# 컴프리헨션 다시 보자
deciding = [[False]*5 for _ in range(5)]

def bingo():
    cnt = 0

    for r in range(5):
        if all(deciding[r][c] for c in range(5)):
            cnt += 1

    for c in range(5):
        if all(deciding[r][c] for r in range(5)):
            cnt += 1

    if all(deciding[i][i] for i in range(5)):
        cnt += 1
    
    if all(deciding[i][4-i] for i in range(5)):
        cnt += 1

    return cnt

pos = {}
for r in range(5):
    for c in range(5):
        pos[board[r][c]] = (r, c)

for idx, x in enumerate(nums, 1):  # enumerate의 두번째 인자는 인덱스 시작 번호를 의미한다
    r, c = pos[x]
    deciding[r][c] = True

    if bingo() >= 3:
        print(idx)
        break

'''
1. all 내장함수 학습
 # 반복할 수 있는 객체를 인자로 받으며 모든 반복이 True 를 반환할때 True 를 반환한다
 # 위 함수에서 all 이 사용된 부분을 구현하기 위해 처음에 그냥 생으로 반복문을 전부 다 돌렸는데
 # 그럴 필요 없이 단 한 줄의 코드로 표현 가능

2. 딕셔너리의 추가적인 이용방법 학습
 # 좌표를 키값으로 데이터를 기록하는 부분은 연습하고 있었는데 이 빙고 문제는 반대로
 # 데이터를 키값으로 좌표를 밸류로 기록한다. 그래서 추후 데이터의 위치를 추적하기가 용이함.

3. enumerate 의 추가 매개변수 확인
 # 지금까지 그냥 enumerate를 리스트를 인자로 받아서 인덱스와 밸류를 튜플로 뽑아주는 함수
 # 라고만 알고 있었는데 인덱스의 시작 번호를 지정할 수가 있었다.
 # 만약 위 enumertate 의 두번째 인자가 3이 된다면 리스트의 0 번 인덱스는 3 번 인덱스로 출력되기 시작하는 것
 # 직접 실험해보기도 헀고 Docs 에서 확인한 내용이니 믿어도 좋다.
'''
