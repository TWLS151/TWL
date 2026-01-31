---
title: "여러번의 append를 객체로 리펙토링"
date: 2026-01-26
tags: [python]
authors: jsc
description: "26-01-25"
---


- Situation
26-01-25
ws-04-06
append로 list에 추가를 하는데 추가 내용이 너무 많아서 코드가 더러워짐
```py
  parsed_data = response.json()

dummy_data.append({'company': parsed_data.get('company').get('name')})

dummy_data.append({'lat': parsed_data.get('address').get('geo').get('lat')})

dummy_data.append({'lng': parsed_data.get('address').get('geo').get('lng')})

dummy_data.append({'name': parsed_data.get('name')})
```
- Task
여러줄에 걸친 비효율적인 append 코드를 줄이고, 한번에 묶어서 처리하는 깔끔한 로직 필요
- Action
  객체화를 통해서 단일 append
```py
user_node = {
    'company': parsed_data.get('company').get('name'),
    'lat': geo.get('lat'),
    'lng': geo.get('lng'),
    'name': parsed_data.get('name')
}
dummy_data.append(user_node) 
```
- Result
  - 코드 효율성: append 횟수 줄임
  - 가독성 향상