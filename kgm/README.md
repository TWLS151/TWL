# SSAFY 1주차 배운 점들
## 개념들
* 표현식 : 하나의 '값'으로 평가될 수 있는 모든 코드
* 값 : 표현식이 평가된 결과, 더이상 계산되거나 평가될 수 없는 가장 기본적인 데이터 조각
** 모든 값은 그 자체로 가장 단순한 표현식이지만 모든 표현식이 값인 것은 아니다 **
* 문장 : 특정 '동작'을 지시하는 실행가능한 코드의 최소 단위
* git : 분산 버전 관리 시스템
** 장점 : 중앙 서버에 의존하지 않고도 동시에 다양한 작업을 수행, 중앙 서버의 장애나 손실에 대비하여 백업과 복구가 용이, 인터넷에 연결되지 않은 환경에서도 작업을 계속할 수 있음
* git의 3가지 영역 (Working Directory, Staging Area, Repository)
* Working Directory : 실제 작업 중인 파일들이 위치하는 영역
* Staging Area : 변경된 파일 중 다음 버전에 포함시킬 파일들을 선택적으로 준비시키는 영역
* Repository : 버전 이력과 파일들이 영구적으로 저장되는 영역
* commit 변경된 파일들을 저장하는 행위

## 알고리즘 공부
* 딕셔너리 형태의 데이터를 for 문에 넣으면 ``` for i in {dict} ``` i 에는 key 값만 반환된다. 만약 key와 value를 모두 사용하고 싶다면 ``` for key, value in {dict}.items() ``` 를 사용하면 key에는 키값이 value에는 value 값이 들어간다
* SW Expert Academy 문제 4869번 D2문제  알고리즘    
바닥에 20xN 크기의 직사각형을 가로x세로 길이가 10x20, 20x20인 직사각형을 이용하여 만들 수 있는 경우의 수를 모두 구하는 문제   
* 사고 과정   
1. 짝수와 홀수로 나누어 풀려고 함. But 짝수와 홀수만의 알고리즘으로 나오지 않음
2. 피보나치 수열과 같은 재귀적인 성격을 띄는지 분석, 그렇지 않았음
3.  20 * 20의 개수가 늘어남에 따라 가능한 경우의 수를 계산하는 알고리즘으로 생각 전환 (전체)!/(20 *20의 갯수)! *(20 * 10의 갯수 )! 로 경우의 수를 구함   
 20 * 20 은 그대로와 가로로 반이 나뉘는 경우 2가지가 있어 수만큼 2를 제곱함, while문으로 전체 길이보다 작은 경우까지만 계산하도록 만듦




 ``` python
N=int(input())
n=int(N/10)
result=0
    a=0 # 20*20이 하나도 없을때부터 시작
    while (a*2)<=n: # 20*20의 개수가 전체보다 크지 않게 하기 위함
        b=n-(a*2)
        cases = math.factorial(n-a)/(math.factorial(a) * math.factorial(b)) # (전체)!/(20 *20의 갯수)! *(20 * 10의 갯수 )!
        cases=cases*(2**a) # 20*20의 경우의 수는 2
        result+=cases
        a+=1
    print(f'#{test_case} {int(result)}')
```

다른 위치에 있는 파일 불러오기
```python
# open 및 json 모듈 사용예시

# JSON 형식의 파일을 처리하기 위한 내장 모듈
import json

# 파일 시스템 경로를 객체 지향적으로 다루기 위한 모듈
from pathlib import Path

# 현재 실행 중인 파일의 절대 경로를 기준으로 부모 디렉토리 경로 설정
# - Path(__file__): 현재 파일의 경로를 Path 객체로 변환
# - resolve(): 실제 경로로 변환하고 절대 경로를 반환
# - parent: 부모 디렉토리 경로를 반환
current_dir = Path(__file__).resolve().parent


# 파일 열기
# open('파일경로', encoding='인코딩방식')
# - current_dir / 'sample.json': Path 객체의 / 연산자로 경로 결합
# - encoding="utf-8"은 한글 등 유니코드 문자를 올바르게 처리하기 위한 설정
movie = open(current_dir / 'sample.json', encoding='utf-8')

# json.load()로 JSON 파일의 내용을 파이썬 데이터로 변환
# - JSON의 object → 파이썬 딕셔너리
# - JSON의 array → 파이썬 리스트
# - JSON의 string → 파이썬 문자열
# - JSON의 number → 파이썬 정수/실수
movie_detail = json.load(movie)

# 변환된 파이썬 데이터 출력
print(movie_detail)
# 파이썬 딕셔너리로 변환됨을 확인
print(type(movie_detail))
```



## 개선할점
- 첫째로 낭비하는 시간이 많았음, 컨디션 관리 실패로 피곤해서 코딩 연습하지 않고 잠을 잔 경우가 많았음.
- 둘째로 대부분의 문제를 for문을 사용해서 풀려고함. 가장 익숙한 방식이지만 이것만으로는 모든 문제 해결에 무리가 있을 수도 있음. 당장에는 크게 문제가 되지는 않음.
- 셋째로 문제를 이해하는데 시간이 오래 걸린다. 계속해서 다양한 문제를 봐야겠다.

## 현재 풀고 있는 문제 
- 파리잡기 (x표시 알고리즘 생각하기)