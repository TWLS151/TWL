# '''
# 10진수 -> 2진수,
# 2진수 -> 10진수로의 변환 실습 코드 (내장함수 사용 X)
# '''

# decimal_hexadecimal = {

#     10 : 'A',
#     11 : 'B',
#     12 : 'C',
#     13 : 'D',
#     14 : 'E',
#     15 : 'F',
# }

# hexadecimal_decimal = {

#     'A' : 10,
#     'B' : 11,
#     'C' : 12 ,
#     'D' : 13 ,
#     'E' : 14,
#     'F' : 15,
# }

# # 1. 10진수 -> 16진수로의 변환

# # 원하는 진수에 맞게 나누는 수를 조정
# # 16진수의 경우는 10 ~ 15까지의 알파벳을 딕셔너리로 관리

# target_decimal = 432
# binary_num = []

# while target_decimal > 0:       # 0보다 클 때 동안

#     bit = target_decimal % 16    # 주어진 수를 2로 나눈 나머지 = 비트

#     if bit >= 10:

#         bit = decimal_hexadecimal[bit]

#     binary_num.append(bit)  # 비트를 2진수 리스트에 할당

#     target_decimal //= 16        # 주어진 수를 2로 나눈 몫 할당

# else: 

#     binary_num.reverse()    # <핵심> 할당된 비트 순서를 뒤집어야 2진수 변환이 됨
#                             # 2진수의 앞 자리로 갈 수록 곱해지는 2는 누적됨
#                             # "뒤에서부터 채운다"

# print("".join(map(str, binary_num)))


# # 2. 16진수 -> 10진수로의 변환

# target_binary = '1B0' # 111

# hexa_num = 0

# for bit in target_binary: # 각 자리수에 대해

#     hexa_num *= 16         # 2를 곱해서 자릿수 이동

#     if bit.isdecimal():    # 자리수가 정수형이라면 -> 그대로 더하기

#         hexa_num += int(bit)

#     else:
#         bit = hexadecimal_decimal[bit]

#         hexa_num += bit

# print(hexa_num)


'''
진수 변환 (내장함수 활용)
'''

# 1. int() 활용 -> 10진수로 변환

print(int('0x1B0', 16)) # 0b : 2, 0o : 8, 0x : 16진수
print(int('1011', 2))

# 2 bin, oct, hex 함수 활용 -> 타 진법 문자열

print(bin(15)[2:])  # 앞의 '0b', '0x'등을 생략하는 방법
print(oct(15))
print(hex(15))

# 3. format
# 접두어 없는 순수 진법 문자열
# 자릿수 맞출 때
# '0xN`: x자리 N진수로 표기, 남은 부분은 0으로 채우기

num = 15

print(format(num, '011b'))
print(format(num, '06o'))
print(format(num, '04X')) # 대문자로 쓰는 방법


#4. zfill() - 매개변수로 자리수 쉽게 채우기


num = 13

binary_str = bin(num)[2:].zfill(8)

print(binary_str)


# 5. 10진수를 거쳐가기
# 16진수 A7 -> 10진수 -> 2진수 
# 파이썬에서 가장 간결하고 안전

decimal_value = int('A7', 16)

print(f"16진수 A7 -> 10진수 : {decimal_value}")

binary_str = bin(decimal_value)

print(f"10진수 {decimal_value} -> 2진수 : {binary_str[2:]}")