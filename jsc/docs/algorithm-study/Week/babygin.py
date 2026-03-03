import sys
from itertools import combinations

sys.stdin = open('babygin.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input)
    str_a = input()
    counting_list = [0] * 10
    done_1 = False
    done_3 = False
    babygin_done = False

    # [0, 0, 0, 0, ...0] 리스트 생성이후
    # 카운팅 배열처럼 그 위치에 1 추가
    for num in str_a:
        int_num = int(num)
        counting_list[int_num] += 1

    # any라는것을 배워서 써보고 싶다..!
    if any(i == 3 for i in counting_list):
        done_3 = True
    
    # 연속된 3개 숫자 체크
    for i in range(10):
        if counting_list[i] ==1 and counting_list[i+1] ==1 and counting_list[i+2] ==1:
            done_1 = True

    # 3개 연속이 존재, 3개가 중복된거 존재
    if done_1 == True and done_3 == True:
        babygin_done = True
    
    print(babygin_done)

 