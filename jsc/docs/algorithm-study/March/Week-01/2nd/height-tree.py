# 에러가 나는 원인은 극단적인 케이스 같다.
# 차이가 1이 나는 것들이 많은거?

# ===
# 완전 탐색으로 모든 경우의 수 돌리기.
# 그런데 언제까지 물을 줄 수 있느냐가 문제이다. 
# 나무의 수가 많아지면 그냥 다음턴 이렇게 기다릴 수 가 없다
# 그러면 어떻게 해야하지?
# 나무의 개수가 100개 이하이다 라고 나와있으니깐 100번 아니 200번을 돌리면 된다.
# 그런데 이거는 멋이 없어
# 그리고 다시 생각을 하니 200번도 부족해보인다.

# 나무의 최대 높이와의 차이를 리스트로 둔다.
# 이 값이 홀수일 때 그리고 짝수 일때를 구분을 한다.
# 만약 홀수의 횟수와 짝수의 횟수가 불균형을 이루게 된다면
# 이것은 조정이 필요하다.
# 짝수가 많다. -> 홀수를 여러날로 나누어서 붓는다.
# 대신 2일차씩 합쳐서 계산을 해야한다.
# 홀수가 많다. -> 어쩔수 없다.
# 그러면 일단 차이가 1이 될 때까지 풀면된다.

# 이 풀이 선택!!!!!!!1
# 이거 조합으로도 풀릴것 같은데?
# 중복이 있는 조합으로 풀면 되잖아? 이게 제일 빠를 것 같다.
# 2, 1 두개만 뽑아내면 되고
# 두개의 개수의 차이를 최소가 되는 것을 찾아야한다.
# 일단 홀수인것들은 1을 먼저 다 뿌린다.
# 그리고 남은것들은 2와 1을 분배를 하면 될듯하다.

from itertools import product
import sys

sys.stdin = open('height-tree.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    trees = list(map(int, input().split()))
    odd_trees = []
    tree_gaps = []
    offset_trees = []
    cnt = 0
    # print(trees)

    highest_tree = max(trees)
    # print(highest_tree)
    # 최고 높이와의 차이가 홀수인 것들의 인덱스를 저장. 값을 저장을 하지 않는 이유는 같은 값이 중복으로 나올까봐
    # 이거 enumerate쓰자. 일단 나중에
    # offset_trees를 만들어서 차이가 홀수인 것들을 1을 빼준 리스트를 생성을 한다.
    for tree_idx in range(len(trees)):
        odd_gap_tree = trees[tree_idx]
        if (highest_tree - odd_gap_tree) % 2 == 1:
            # odd_trees 리스트 값들은 무조건 홀수 날에 줘야함.
            odd_trees.append(tree_idx) 
            offset_trees.append(highest_tree - (trees[tree_idx] -1 ))
            cnt += 1
        
        else:
            offset_trees.append(highest_tree - trees[tree_idx])

    # print(offset_trees)
    # print(odd_trees)
    # print(sum(offset_trees))
    # print(cnt)
    ## 이제 이 offset리스트
    # 만약에 10이라는 숫자가 있어. 이것을 1, 2로 분배를 하는 최소는 3을3번을 하고 1을 한번 더 하는거야
    # 그런데 문제는 cnt에 쓴만큼 1을 썼다는거야.
    # cnt가 2라는것은 1을 두번을 썼다는 것이고 나는 강제로 2를 2번을 쓰고 시작을 해야한다.
    # 2를 쓰지 못하는 경우랑 아닌경우랑 구분을 해야한다. while을 쓰면 될듯
    # (sum(offset_trees) - cnt * 2) // 3
    # (sum(offset_trees) - cnt * 2) % 3 
    # 나머지 0인경우 굳
    # 나머지 1인경우 하루 추가
    # 나머지 2인 경우 2일 추가
    if (sum(offset_trees) - cnt * 2) < 0:
        print('error')
    else:
        cnt += ((sum(offset_trees) - cnt * 2) // 3) * 2
        if (sum(offset_trees) - cnt * 2) % 3 == 2:
            cnt += 2
        elif (sum(offset_trees) - cnt * 2) % 3 == 1:
            cnt += 1
        # print(cnt)


    # print(odd_trees)

    for tree_idx in range(len(trees)):
        curr_tree = trees[tree_idx]
        gap = highest_tree - curr_tree
        tree_gaps.append(gap)
    sorted_tree_gaps = sorted(tree_gaps)
    # print(sorted_tree_gaps)

    cnt_new = 0
    new_new_list = []
    for tree in sorted_tree_gaps:
        cnt_new += (tree // 3)
        new_new_list.append(tree % 3)
    print(cnt_new * 2)
    print(new_new_list)
    
    one = 0
    two = 0
    for tree in new_new_list:
        if tree == 1:
            one += 1
        elif tree == 2:
            two += 1

    if one == two:
        cnt_new += one * 2
    elif one == two + 1:
        cnt_new = one + two
    elif one > two:
        cnt_new = (one - two) * 2 + (one - two + 1)
    elif two > one:
        cnt_new = one * 2 + (two - one)*2

    print(one)
    print(two)
    print(cnt_new)
    # print(cnt)
    # 1 8
    # 2 5



# 일단 가장 큰 값을 찾기


# 가장 큰값과 차이가 홀수 인것을 찾기


# 7개 
# 