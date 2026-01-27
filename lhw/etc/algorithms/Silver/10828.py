# 입력값에 들어있는 문자열에 따라 다른 작업을 수행하는 stack 구현하는 문제
# 시간제한이 있어 sys 모듈을 사용했으나 없어도 큰 차이는 없었을 듯함

import sys
input = sys.stdin.readline

stacks = []
def stack(strs: str):
    if 'push' in strs:
        stacks.append(int(strs[5:]))
    elif 'top' in strs:
        if stacks:
            print(stacks[-1])
        else:
            print(-1)
    elif 'size' in strs:
        print(len(stacks))
    elif 'empty' in strs:
        if stacks:
            print(0)
        else:
            print(1)
    elif 'pop' in strs:
        if stacks:
            print(stacks.pop())
        else:
            print(-1)

tc = int(input().strip())
for _ in range(tc):
    stack(input().strip())
