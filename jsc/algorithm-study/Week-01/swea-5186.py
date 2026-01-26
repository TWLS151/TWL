
# ---
# 4번째(최신)
# ---

T = int(input())
for _ in range(1,T+1):
    result = ''
    n = float(input())
    i = 1
    while n > 0:
        if i == 13:
            print('overflow')
            break
        if n >= 2**(-i):
            result += '1'
            n -= 2**(-i)
            i += 1
            print(result)
        else: 
            result += '0'
            i += 1
            continue
            

print(result)




# ---
# 아카이브


# ---
# 1번째
# ---

# T = int(input())
# for _ in range(1,T+1):
#     result = []
#     num = int(input())
#     for i in # num = 0 까지:
#         if num - 2**(i) < 0:
#             result.append('1')
#         else:
#             result.append('0')
#             num -= 2**(i)

# print(f"#{T} {*{result}}")


## 내가 모르는 것
# for문을 언제 끝나는지 지정
# 리스트의 값들을 대괄호없이



# ---
# 2번째
# ---

# T = int(input())
# for _ in range(1,T+1):
#     result = []
#     n = float(input())
#     i = 1
#     while n >= 0:
#         if n == 0:
#             print(*result)
#             break
#         if i == 13:
#             print('overflow')
#             break
#         result.append(1)
#         n -= 2**(-i)
#         i += 1
#         print(*result)
#     else:
#         result.append(0)
#         n -= 2**(-i)
#         print(*result)
#         i += 1

# print(*result)


## 내가 모르는 것
# for문을 언제 끝나는지 지정
# 리스트의 값들을 대괄호없이

# ---
# 3번째
# ---

# T = int(input())
# for _ in range(1,T+1):
#     result = ''
#     n = float(input())
#     i = 1
#     while n > 0:
#         if i == 13:
#             print('overflow')
#             break
#         if n >= 2**(-i):
#             result += '1'
#             n -= 2**(-i)
#             i += 1
#             print(result)
#         else: 
#             result += '0'
#             a = n
#             n -= 2**(-i)
#             i += 1
#             print(result)
#             if n <0:
#                 n -= 2**(-i)
#                 result += '1'
#             else:
#                 result += '0'
# print(result)





# ---
# 1번째
# ---

# T = int(input())
# for _ in range(1,T+1):
#     result = []
#     n = float(input())
#     i = 1
#     while n >= 0:
#         if n == 0:
#             print(*result)
#             break
#         if i == 13:
#             print('overflow')
#             break
#         result.append(1)
#         n -= 2**(-i)
#         i += 1
#         print(*result)
#     else:
#         result.append(0)
#         n -= 2**(-i)
#         print(*result)
#         i += 1

# print(*result)


## 내가 모르는 것
# for문을 언제 끝나는지 지정
# 리스트의 값들을 대괄호없이

# ---
# 2번째
# ---

# T = int(input())
# for _ in range(1,T+1):
#     result = ''
#     n = float(input())
#     i = 1
#     while n > 0:
#         if i == 13:
#             print('overflow')
#             break
#         if n >= 2**(-i):
#             result += '1'
#             n -= 2**(-i)
#             i += 1
#             print(result)
#         else: 
#             result += '0'
#             a = n
#             n -= 2**(-i)
#             i += 1
#             print(result)
#             if n <0:
#                 n -= 2**(-i)
#                 result += '1'
#             else:
#                 result += '0'
# print(result)

# T = int(input())
# for _ in range(1,T+1):
#     result = ''
#     n = float(input())
#     i = 1
#     while n > 0:
#         if i == 13:
#             print('overflow')
#             break
#         if n >= 2**(-i):
#             result += '1'
#             n -= 2**(-i)
#             i += 1
#         else: 
#             result += '0'
#             i += 1
#             continue
            

# print(result)