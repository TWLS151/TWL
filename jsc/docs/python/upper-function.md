---
title: "upper function은 원본을 바꾸지 않는다"
tags: [python]
authors: jsc
description: "def capitalize_words(a):"
---


```PY
# 아래 함수를 수정하시오.
def capitalize_words(a):
    name = ''
    for i in range(len(a)):
        if  i == 0:
            
            name += a[i].upper()
        elif a[i-1] == ' ':
            
            name += a[i].upper()
        else:
            name += a[i]

    return name


result = capitalize_words("hello, world!")
print(result)
```
```PY
# 아래 함수를 수정하시오.
def capitalize_words(a):
    name = ''
    for i in range(len(a)):
        if  i == 0:
            a[i].upper()
            name += a[i]
        elif a[i-1] == ' ':
            a[i].upper()
            name += a[i]
        else:
            name += a[i]

    return name


result = capitalize_words("hello, world!")
print(result)
```