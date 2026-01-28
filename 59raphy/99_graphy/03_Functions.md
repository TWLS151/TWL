# Functions


## 함수
1. 함수 정의
    > def get_sum():

    >   return
2. 함수 호출
    - 함수의 이름과 소괄호 활용해 호출
    - 필요한 경우 인자 전달 -> 매개변수에 대입
    > result = get_sum(1, 2)
3. 결과 확인
    > print(result)

**함수 구조**
- 정의부(def) ; 아래로 들여쓰기
    - 함수 이름
    - 매개변수(parameter) ; input
    - 콜론(:)
- function body
    - Docstring(""" """) ; 함수 설명서
    - 반환값(return value) ; output
        - return문이 없으면 None 반환


## 매개변수와 인자
- 매개변수(parameter) : 함수 정의 시 함수가 받는 값
- 인자(argument): 함수 호출 시 함수에 전달하는 값

### 인자
1. 위치 인자
    - 함수 호출 시 위치에 따라 인자 전달
2. 기본 인자
    - 함수 정의 시 매개변수에 기본값 할당
3. 키워드 인자
    - 함수 호출 시 인자의 이름과 함께 값을 전달
        > greet(name='Dave', age=35)
    - 인자 순서 상관 x
    - *호출 시 키워드 인자는 위치 인자 뒤로*
4. 임의의 인자 목록
    - 인자의 개수가 정해지지 않은 경우
    - 함수 정의 시 매개변수 앞에 '*'를 붙임
    - 여러 개의 인자를 *tuple*로 처리
        > def get_sum(*args)
5. 임의의 키워드 인자 목록
    - 키워드 인자의 개수가 정해지지 않은 경우
    - 함수 정의 시 매개변수 앞에 '**'를 붙임
    - 여러 개의 인자를 *dictionary*로 처리
        > def print_info(**kwargs)

- 함수 인자 권장 작성 순서
    : 위치 -> 기본 -> 가변 -> 가변 키워드


## 재귀 함수
- 1개 이상의 base case
- 종료 조건 명확히 할 것
    - 스택 오버플로우 에러 발생 우려


## 내장 함수 (Built-in function)
- len(numbers)
- max(numbers)
- min(numbers)
- sum(numbers)
- sorted(numbers, reverse=True)
    - reverse=False : 오름차순(기본값)
    - reverse=True : 내림차순


## 함수와 Scope
- 변수의 수명주기
    - local scope의 변수는 global scope에서 사용할 수 없음
- 이름 *검색* 규칙 : LEGB Rule
    - 함수 내에서는 바깥 scope의 변수에 접근 가능하나 *수정은 할 수 없음*
    - 바깥 scope에서 안쪽 scope의 변수에 접근할 수 없음
    - 바깥 scope와 동일한 변수명을 안쪽 scope에서 사용하면 기존에 바깥의 변수에 할당된 값은 사용 불가

### global 키워드
- 변수의 scope를 전역 범위로 지정
- 함수 내에서 전역 변수 수정 위해 사용
- global 키워드 선언 전에 참조 불가
- 매개변수에는 global 키워드 사용 불가


## 함수 스타일 가이드

### 함수 이름 작성 규칙
- 동사[_형용사]_명사
- get/set_명사
- True/False 반환할 경우 is/has로 시작

### 단일 책임 원칙
- 모든 객체는 하나의 명확한 목적과 책임만을 가져야 함
- 책임을 분리하여 역할 하나당 함수 하나씩 만들고 메인 함수에서 순차적으로 실행


## Packing & Unpacking

### Packing
- 여러 개의 값을 하나의 *튜플*로 묶음
- 함수 *정의* - 매개변수 작성 시
    - 남는 위치 인자들을 튜플로 묶음
    - 남는 키워드 인자들을 딕셔너리로 묶음
- print 함수는 임의의 가변 인자 여러 개를 받을 수 있음
    - 인자 개수에 상관 없이 튜플 하나로 패킹되어 내부에서 처리
    > print(*objects)

### Unpacking
- 시퀀스 언패킹 / 다중 할당
- 튜플이나 리스트 등의 객체의 요소들을 개별 변수에 할당
- 함수 *호출* - 인자 전달 시
    - 리스트나 튜플 앞에 *를 붙여 각 요소를 함수의 개별 위치 인자로 전달
    - 딕셔너리 앞에 **를 붙여 {키: 값} 쌍을 키=값 형태의 키워드 인자로 전달


## 참고

### 함수와 반환
- 함수는 단 하나의 값(객체)만 반환
- 여러 값을 반환하는 경우 하나의 튜플로 패킹하여 반환
    > def get_user_info():
    
        return name, age
    > print(user_data)  # ('Alice', 30)

### 람다 표현식
> def addition(x, y):

>   return x + y

lambda 매개변수: 표현식
> lambda x, y: x + y

- sorted 함수의 key 매개변수에 활용
