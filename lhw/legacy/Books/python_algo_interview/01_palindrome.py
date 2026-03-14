# 입력 문자열이 펠린드롬인지 확인하는 문제
# 편의상 입력은 밑에 고정해뒀다

# 리스트 활용 풀이

def isPalindrome(s: str) -> bool:
    strs = []
    for char in s:
        if char.isalnum():
            strs.append(char.lower())
    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False
    return True

#-------------------------------------#

# 데크 (Deque) 활용 풀이

import collections
from collections import deque

def isPalindrome(s: str) -> bool:
    strs: deque = collections.deque() # collections.deque()

    for char in s:
        if char.isalnum():
            strs.append(char.lower())
    
    while len(strs) > 1:
        if strs.popleft() != strs.pop(): # .popleft()
            return False
    return True

#--------------------------------------#

#슬라이싱 활용 풀이

import re

def isPalindrome(s: str) -> bool:
    s = s.lower()
    s = re.sub('[^a-z0-9]', '', s) # re.sub()

    return s == s[::-1]

#--------------------------------------#

print(isPalindrome('race car')) # True
print(isPalindrome('good')) # False

#----------------------------------------#

'''
총 세가지 풀이
아래로 갈 수록 더 성능이 좋아지며 파이썬다운 방식이라고 한다.

- 우선 공부를 할 수록 점점 많이 보이는 collections 모듈
위에 쓰인 deque를 끌어올 수 있고 deque는 위에서 30번 라인에 있는 popleft()를 가능하게 하는데 아마 pop(0)의 기능을 하는 듯 하다.
deque 메서드를 사용하려면 26번 라인에서 한 것처럼 데이터 구조를 collections.deque()로 바꿔야하는 듯
최근 자주 보이는 defaultdictionary 함수 또한 collections 모듈에 들어있어 자세히 공부해봐야할 듯 하다.

- 다음 re 모듈
regex 모듈이다.
정규식을 불러오는데 게임에서만 사용하던 정규식이 게임 외에서도 사용한다는 걸 처음 알았다.
조금 생각해보면 당연하긴 한데.. 아무튼
정규식을 사용할 수 있다.
re.sub(pattern, new, target)
target에 존재하는 pattern 을 new 로 대체하는 메서드? 인데
문자열 메서드인 replace와의 차이점은 pattern이 위 코드처럼 정규식으로 범위표현이 가능하다는 점이다.
위 [^a-z0-9] 를 replace로 나타내려면
s.replace(a,b,c,d,e,f,...,z,0,1,2,3,~, new) 으로 가야하기 때문에 사용 할 수 있다면 하지 않을 이유가 없다.
[] 안이 패턴을 넣을 수 있고 ^는 not을 의미한다.
s 문자열 안의 알파벳과 숫자가 아닌 문자열은 ''으로 대체한다는 의미
'''