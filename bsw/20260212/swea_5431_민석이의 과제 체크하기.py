import sys

sys.stdin = open('swea_5431_민석이의 과제 체크하기.txt')

def bubble_sort(a):
    for i in range(len(a)-1, 0, -1):
        for j in range(i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

T = int(input())
for tc in range(1, T + 1):
    stu_num, M = map(int, input().split())
    submit_n = list(map(int, input().split()))
    n_lst = []
    for i in range(1, stu_num + 1):
        n_lst.append(i)
    result_lst = []
    for j in range(len(n_lst)):
        if n_lst[j] not in submit_n:
            result_lst.append(n_lst[j])
                

    
    print(f'#{tc}', *result_lst)