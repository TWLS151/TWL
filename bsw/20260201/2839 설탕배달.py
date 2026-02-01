T = int(input())
num = 0
# 봉지 기록할 변수 지정
while T >= 0:
# T값을 모두 소모할 때 까지 반복
    if T % 5 == 0:    
        num += (T // 5)
        print(num)
        break
    # T가 5로 나누어 떨어지면 나눈 몫 반환하고 바로 종료
    T -= 3          
    num += 1
    # 5로 안 나누어지니 일단 3만 빼고 봉지 개수 1개 증가            

else:
    print(-1) 
# 이 모든 경우에 해당하지 않으면 -1 출력


# 아래 풀이 방식은 5로 나눈 나머지 값에 따른 봉지 개수를 
# 계산하려 했으나 너무 if 문이 많아지는 것 같아서 
# 다른 방법 모색함.

# T = int(input())
# if T % 5 == 0:
#     print(T // 5)
# elif T % 5 == 3:
#     print(T // 5 + 1)
# elif T % 5 == 2:
#     if T == 2 or T == 7:
#         print(-1)
#     elif T % 3 == 2:
#         print(T // 3)
#     elif T % 3 == 0:
#         print(T // 3)
# elif T % 5 == 1:
#     if T == 1:
#         print(-1)
#     else:
#         print(T // 5 + 1)
# elif T % 5 == 4:
#     if T == 4:
#         print(-1)
#     else:
#         print(T // 5 + 2)
# elif T % 8 == 0:
#     print(T // 8 * 2)

# elif (T % 5) % 3 != 0 or T % 3 != 0:
#     print(-1)


