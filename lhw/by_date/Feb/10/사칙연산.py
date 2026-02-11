# SWEA - 1232
# 사칙연산

import sys
sys.stdin = open('사칙연산.txt')

def calc(node_idx):
    #
    if len(tree_info[node_idx]) == 2:
        return int(tree_info[node_idx][1])
    
    else:
        left_child_idx = int(tree_info[node_idx][2])
        right_child_idx = int(tree_info[node_idx][3])

        left_val = calc(left_child_idx)
        right_val = calc(right_child_idx)

        op = tree_info[node_idx][1]
        if op == '+':
            return left_val + right_val
        elif op == '-':
            return left_val - right_val
        elif op == '*':
            return left_val * right_val
        elif op == '/':
            return left_val // right_val

    pass


# T = int(input())

for test_case in range(1, 11):
    T = int(input())
    tree_info = [[] for _ in range(T + 1)]
    for _ in range(T):

        node_input = input().split()

        tree_info[int(node_input[0])] = node_input

    result = calc(1)

    print(f'#{test_case} {result}')