# BOJ - 14888
# 연산자 끼워넣기

# 1. 상태 정의
'''
연산자의 선택 현황 // 남은 연산자의 갯수
'''
# 2. 선택
'''
남은 연산자 중 하나를 선택한다
'''
# 3. 제약
'''
연산자의 우선순위는 무시하고 앞에서부터 계산한다.
'''
# 4. 백트래킹 ( 필요 시 )
'''
계산이 끝나면 그 계산에서 사용된 연산자 갯수를 다시 되돌린다.
'''

N = int(input())  # 숫자의 갯수
nums = list(map(int, input().split()))  # 연산을 진행해야하니 정수로
# 앞에서부터 계산해야하는데 그럼 뒤집어서 뒤에서부터 계산하는 것도 괜찮겠다.
nums.reverse()

# 순서대로 + - * // [0, 1, 2, 3]
op_lst = list(map(int, input().split())) 

max_val = float('-inf')
min_val = float('inf')



# [0: +, 1: -, 2: *, 3: //] #
def dfs(nums, op_lst):
    global max_val, min_val

    # 기저: 남은 연산자가 없으면 종료
    if len(nums) == 1:
        max_val = max(max_val , nums[0])  # 진입
        min_val = min(min_val , nums[0])  # 진입
        return

    # 반복
    for idx in range(4):
        if op_lst[idx] != 0:  # 연산자가 남아있으면
            op_lst[idx] -= 1  # 하나 사용
            nnums = nums[:]
            if idx == 0:
                adds = nums.pop() + nums.pop()
                nums.append(adds)
            elif idx == 1:
                adds = nums.pop() - nums.pop()
                nums.append(adds)
            elif idx == 2:
                adds = nums.pop() * nums.pop()
                nums.append(adds)
            else:
                adds = int (nums.pop() / nums.pop())
                nums.append(adds)
            
            dfs(nums, op_lst)

            op_lst[idx] += 1  # 계산 끝나면 되돌림
            nums = nnums[:]

dfs(nums, op_lst)

print(max_val)
print(min_val)