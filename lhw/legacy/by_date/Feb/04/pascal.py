# SWEA - 2005


TC = int(input())

for test_case in range(1, TC + 1):
    num_of_line = int(input())

    # 인덱스로 풀어야겠는데?
    # 이전 리스트의 본인 인덱스 + 이전 리스트의 인덱스-1

    pascal = [[1] * i for i in range(1, num_of_line + 1)]

    # print(pascal)

    for idx in range(2, num_of_line):
        for i in range(1, len(pascal[idx]) - 1):
            pascal[idx][i] = pascal[idx-1][i-1] + pascal[idx-1][i]
    
    # unpack = *pascal

    print(f'#{test_case}')
    for lst in pascal:
        print(*lst)
