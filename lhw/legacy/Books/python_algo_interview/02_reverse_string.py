# Two pointer

def reverse_string(s: list[str]):
    left, right = 0, len(s) - 1 # 왼쪽은 인덱스 0부터 오른쪽은 마지막 인덱스(s - 1) 부터
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return s

# --------------------------------------- #

# Like Python

def reverse_string(s: list[str]):
    s.reverse()
    return s

#------------------------------------------#

# slicing

def reverse_string(s: list[str]):
    return s[::-1]


#-------------------------------------------#

# print
s = ['h', 'e', 'l', 'l', 'o']
print(reverse_string(s))

#-------------------------------------------#

'''
문자열 뒤집는 방법 세 가지

밑의 두개는 메서드와 슬라이싱을 이용한 방법으로 파이선에서 가능한 방식이고
첫 번째의 투포인터 방식은 고전적인 알고리즘 풀이라고 소개되어 있다.

각 양 끝에서부터 연산할 때마다 한 칸씩 안쪽으로 들어오며 연산을 하는? 그런 느낌인데 이 책에서 많이 소개되는 것 같고 볼수록 매력적인 알고리즘이라 연습하려한다.
while 문을 이용하기 때문에 종료조건도 확인해주고 하나씩 순서를 바꾸는 방식이다.

'''