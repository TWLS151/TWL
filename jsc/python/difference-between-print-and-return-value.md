# print와 return 값의 차이
26-01-26

return이 없을 때 발생하는 에러
```py
def add_print(a, b):
    print(a + b)

result = add_print(3, 5) 
# 화면에는 8이 찍히지만, result 변수에는 아무것도 저장되지 않습니다 (None).def add_print(a, b):
```