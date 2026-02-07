# SWEA - 4613
# 러시아 국기 같은 깃발
# TTP: 58'16"

import sys
sys.stdin = open('like_russian.txt')

TC = int(input())

for test_case in range(1, TC+1):
    height, width = map(int, input().split())
    flag = [input() for _ in range(height)]
    
    min_count = 10**99
    for i in range(height - 2):
        for j in range(i+1, height - 1):

            count = 0

            W = [flag[x] for x in range(i+1)]
            B = [flag[x] for x in range(i+1, j+1)]
            R = [flag[x] for x in range(j+1, height)]

            for w in W:
                count += width - w.count('W')
            for b in B:
                count += width - b.count('B')
            for r in R:
                count += width - r.count('R')
            
            if min_count > count:
                min_count = count
    
    print(f'#{test_case} {min_count}')




    # 직접 칠하는 방식으로는 안되겠다.
    # count = 0
    # min_count = 10**99
    # for i in range(height - 2):
    #     for j in range(i+1, height - 1):
    #         for l in range(i+j+1, height):
    #             for k in range(width):
    #                 if flag[i][k] != 'W':
    #                     flag[i][k] = 'W'
    #                     count += 1
    #                 if flag[j][k] != 'B':
    #                     flag[j][k] = 'B'
    #                     count += 1
    #                 if flag[l][k] != 'R':
    #                     flag[l][k] = 'R'
    #                     count += 1
    #         if min_count > count:
    #             min_count = count
