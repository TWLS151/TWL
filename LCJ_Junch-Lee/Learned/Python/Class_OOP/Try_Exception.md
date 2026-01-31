---
---
## 에러와 예외 (Error & Exception)

- 문법 에러 : `Invalid Syntax`, `assign to literal`
- 예외 : 프로그램 실행 중 오류
    - 내장 예외


### 예외 처리

- 예외가 발생했을 때 프로그램이 비정상적으로 종료되지 않고, 적절하게 처리할 수 있도록 하는 방법

```python 
try : # 예외가 발생할 수 있는 코드 작성

except : # 예외가 발생했을 때 실행할 코드 작성

else : # 예외가 발생하지 않았을 때

finally # 예외 발생 여부와 상관없이 항상 실행할 코드 작성

```

## 참고 파트

### 예외 처리 주의사항

```python
# 0을 입력했을 때, 출력할 구문은?
# ? 

try:
    num = int(input('100으로 나눌 값을 입력하시오'))

except Exception:
    print('0으로 나눌 수 없습니다.')

except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')

except:
    print('에러가 발생하였습니다.')


# except Exception이 모든 예외를 가로채기 때문에, 그 아래에 있는 ZeroDivisionError 전용 코드는 절대 실행되지 않음
```

- 구체적인 예외부터 먼저 except 구문에 작성(처리)하고, 이후 코드로 갈 수록 범용적인 Error로 처리하는 것이 바람직 (마지막 : Exception)

---
---
## 예외 객체 다루기

### as 키워드

- except 블록에서 예외 객체를 받아 상세한 예외 정보를 활용 가능 

### if, else문 사용 가능


### EAFP, LBYL

- EAFP : `try ~ except` 문 사용'

- LBYL : `if ~ else`문 사용
