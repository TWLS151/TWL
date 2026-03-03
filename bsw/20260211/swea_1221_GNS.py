import sys

sys.stdin = open('swea_1221_GNS.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = list(map(str, input().split()))
    num_lst = list(map(str, input().split()))
    str_lst = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    # 배열할 문자 지정
    result = []
    for j in range(len(str_lst)): # str_lst 순회
        for i in range(int(M)): # M을 다시 정수로 바꾸고 진행
            if num_lst[i] == str_lst[j]: # 같은 경우
                result.append(str_lst[j])  # 리스트에 순서대로 추가
    print(f'#{tc}')
    print(*result)