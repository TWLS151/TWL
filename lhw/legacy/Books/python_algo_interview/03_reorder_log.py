
# lambda 와 '+' 연산자 이용

def reorderLogFiles(logs: list[str]):
    letters, digits = [], []
    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)
    
    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
    return letters + digits

print(reorderLogFiles(logs= ["dig1 8 1 5 1","let1 art can","dig2 3 6", " let2 own kit dig","let3 art zero"]))

#---------------------------#

'''
인자로 들어오는 리스트들을 로그의 식별자를 제외한 후 내용들을 기준으로 문자열과 숫자열로 구분한 후 마지막에 리스트의 합연산을 통해 문제를 마무리한다.
명세에 문자열 로그가 숫자열 로그보다 앞에 온다는 내용이 있어 letters + digits 으로 풀이 순서가 바뀌면 둘을 바꾸면 된다.

풀며 함수의 인자 개념이 아직 부족하는 걸 느꼈다. 함수 호출시 리스트 앞에 있는 logs= 의 존재 이유를 몰라 질문을 하기도 했다.
위치 인자, 기본 인자, 키워드 인자, *, ** 의 개념을 다시 잡을 필요가 있다. 추후 정리해서 TIL에 업로드 해야겠다. 

아직 알고리즘을 문제를 풀이하며 로그를 만난 적은 없다. 무슨 의미인지도 무슨 역할을 하는지도 모르지만 책에서 03번 문제로 소개하며
'실무에서도 이 같은 로직은 자주 쓰이는 만큼 매우 실용적인 문제로 볼 수 있다.' 라고 소개하고 있어서 알아둘 필요는 있다고 판단했다.

람다의 개념이 아직 모호하다. 보면 이해는 하겠지만 사용하기는 힘든 수준. 이해도를 더 높일 필요가 있어 보인다.

'''