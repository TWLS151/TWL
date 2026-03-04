# A형 기출
# 나무의 키

import sys
sys.stdin = open('input.txt')

TC = int(input())
for test_case in range(1, TC+1):    
    N = int(input())
    tree_lst = list(map(int, input().split()))

    standard = max(tree_lst)

    if min(tree_lst) == standard:
        print(f'#{test_case} 0')
        continue

    t = 1
    while True:

        if all(i == standard for i in tree_lst):
            print(f'#{test_case} {t}')
            break

        if t % 2 == 0:
            adds = 2
        else:
            adds = 1
        
        mini = min(tree_lst)
        tree_lst.remove(mini)

        if adds == 2 and standard - mini >= 2:
            mini += adds
            tree_lst.append(mini)
        elif adds == 2 and standard - mini < 2:
            tree_lst.append(mini)
            pass

        if adds == 1 and standard - mini >= 2:
            mini += adds
            tree_lst.append(mini)
            
              # ㅇ마 터질듯
        elif adds == 1 and standard - mini == 2:
            mini += adds
            tree_lst.append(mini)

        t += 1