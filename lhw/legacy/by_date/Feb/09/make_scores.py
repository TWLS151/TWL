# IM
# 채점 시스템 만들기

import sys
sys.stdin = open('make_scores.txt')

TC = int(input())

for test_case in range(1, TC+1):
    stu, pro = map(int, input().split())
    ans = list(map(int, input().split()))

    score_list = []
    for stu_ans in range(stu):
        student_answer = list(map(int, input().split()))

        run = 0
        records = 0
        for idx in range(pro):
            if ans[idx] == student_answer[idx]:
                run += 1
                records += run
            else:
                run = 0

        score_list.append(records)

    print(f'#{test_case} {max(score_list) - min(score_list)}')