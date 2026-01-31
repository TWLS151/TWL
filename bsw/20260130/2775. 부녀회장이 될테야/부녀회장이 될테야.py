T = int(input())
for i in range (T):
    a = int(input())
    b = int(input())
    # a : 층수 정의
    # b : 호수 정의
    sum_lst = []
    for l in range(1, b + 1):
        
        sum_lst.append(l)
    # line 7~10 : 0층의 호수를 정의함.[1, 2, 3]을 sum_lst에 추가
    for k in range(a):
        
        for j in range (1 ,b):
            sum_lst[j] += sum_lst[j-1]
    # line 12~15 : 인원을 채우는 과정
    # ex)
    # 0층 :[1, 2, 3]
    # 1층 :[1, 1 + 2, 1 + 2+ 3] by line 15
    # 2층 :[1, 1 + (1 + 2), 1 + (1 + 2) + (1 + 2 + 3)] -> 형식으로 계속 이어짐.
    # ....
    print(sum_lst[-1])
    # 제일 마지막에 있는 리스트 항목을 출력