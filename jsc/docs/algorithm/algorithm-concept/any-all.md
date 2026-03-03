# 조건문 검사할 때 any, all을 사용하자

나는 이 리스트에 True가 하나라도 있는지 판단을 할 때 for-else문을 돌려서 하나씩 확인을 하고
다 돌았을 때 else를 사용을 했다.
그런데 any()또는 all()을 사용을 하면 된다.

if any(n % 2 == 0 for n in nums)