# 암호문3
# 0212 // 1216 - 

# I 삽입 x, y, s : 앞에서부터 x번째 암호문 바로 다음에 y개의 암호문을 삽입한다. s 는 삽입할 암호문
# D 삭제 x, y : 앞에서부터 x번째 암호문 바로 다음부터 y개의 암호문을 삭제한다.
# A 추가 y, s : 암호문 뭉치 맨 뒤에 y개의 암호문을 덧붙인다. s 는 덧붙일 암호문

for test_case in range(1, 11):

    total_num = int(input())
    origin = input().split()
    order_num = int(input())
    order_lst = input().split()

    # 인덱스랑 숫자랑 맞추기
    # origin.insert(0, 0)
    # order_lst.insert(0, 0)
    # 없는게 낫다

    for order in range(order_num -3):
        if order_lst[order] == 'I':
            idx = order_lst[order + 1]
            num = order_lst[order + 2]
            ins_lst = order_lst[order+3 : order+3 + int(num)]
            origin[int(idx):int(idx)] = ins_lst

        elif order_lst[order] == 'D':
            idx = order_lst[order + 1]
            num = order_lst[order + 2]
            del origin[int(idx) : int(idx) + int(num)]

        elif order_lst[order] == 'A':
            num = order_lst[order + 1]
            lst = order_lst[order + 2 : order + 2 + int(num)]
            origin.extend(lst)
            
    print(f'#{test_case}', *origin)

    ## 아우 더러워 안해안해