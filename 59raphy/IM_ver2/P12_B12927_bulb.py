import sys

sys.stdin = open('input_p12_bulb.txt')

# T = int(input())
#
# for tc in range(1, T + 1):
bulbs = list(input())
N = len(bulbs)

def on_off(arr, *n):
    for m in n:
        arr[m] = 'N' if arr[m] == 'Y' else 'Y'

click_cnt = 0

for i in range(N):
    if bulbs[i] == 'Y':
        on_off(bulbs, *[j for j in range(i, N, i + 1)])
        click_cnt += 1

print(click_cnt)


#=================================================================
# ver_1
# 260212

"""
bulb = list(input())
N = len(bulb)

# 1. 초기 상태 변환 ('Y' -> 1, 'N' -> 0)
for i in range(N):
    if bulb[i] == 'Y':
        bulb[i] = 1
    else:
        bulb[i] = 0

switch_cnt = 0

# 2. 그리디 탐색: 1번 전구부터 차례대로 확인
for i in range(N):
    
    # 현재 전구가 켜져 있다면(1) 스위치 누름
    if bulb[i] == 1:
        switch_cnt += 1
        
        # range의 step을 활용하여 i+1의 배수 인덱스만 순회
        # (i)에서 시작하여 N까지 (i+1) 간격으로 점프하며 상태 반전
        for j in range(i, N, i + 1):
            bulb[j] = 1 - bulb[j]
        
        '''
        # 처음 풀이
        M = N // (i + 1)
        for j in range(1, M + 1):
            bulb[(i + 1) * j - 1] = 1 - bulb[(i + 1) * j - 1]
        '''

print(switch_cnt)
"""