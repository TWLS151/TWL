import sys


T = int(sys.stdin.readline())
num_lst = []
# 빈 리스트 생성
for i in range(T):
    word = str(input())
    if word[0:4] == 'push':
        num_lst.append(word[5:])
    # 단어의 앞 4자리가 word면 word의 6번째 자리부터 숫자를 추가(숫자가 10 이상일 경우 대비)    
    elif word[0:5] == 'front':
        if num_lst == []:
            print(-1)
        else:
            print(num_lst[0])
    # front일 때 빈 리스트이면 -1 출력, 아니면 리스트 맨 앞자리 출력
    elif word[0:4] == 'size':
        print(len(num_lst))
    # size일때에는 정수 갯수 출력
    elif word[0:5] == 'empty':
        if len(num_lst) == 0:
            print(1)
        else:
            print(0)
    # empty일때는 리스트 비어있을 때는 1 출력, 아니면 0
    elif word[0:3] == 'pop':
        if len(num_lst) == 0:
            print(-1)
        else:
            pop_num = num_lst.pop(0)
            print(pop_num)
    # pop일때 리스트가 비어있으면 -1 출력, 아니면 맨 앞의 정수 빼내고 그것을 출력
    elif word[0:4] == 'back':
        if len(num_lst) == 0:
            print(-1)
        else:    
            print(num_lst[-1])
    # back일 경우에 정수가 없으면 -1, 아니면 가장 뒤의 정수를 출력
