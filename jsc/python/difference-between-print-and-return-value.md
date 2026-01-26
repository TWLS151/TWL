# print와 return 값의 차이
26-01-26

return이 없을 때 발생하는 에러
```py
def add_print(a, b):
    print(a + b)

result = add_print(3, 5) 
# 화면에는 8이 찍히지만, result 변수에는 아무것도 저장되지 않습니다 (None).def add_print(a, b):
```


## 실제 잘못 적은 코드
```py
def count_character(a, b):
    a.count(b)
    return 


result = count_character("Hello, World!", "o")
print(result)  # 2
```
에러가 난 이유: return값에 아무것도 넣지 않아 None가 나온다. return에 변수만 넣어봐서 매서드나 함수도 넣을 수 있다는 것을 몰랐다.

## 수정된 코드
```py
def count_character(a, b):
    return a.count(b)


result = count_character("Hello, World!", "o")
print(result)  # 2
```