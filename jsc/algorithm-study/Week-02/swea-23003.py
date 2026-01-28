T = int(input())
list = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
for i in range(1, T+1):
    a, b = map(str, input().split())

    a_index = list.index(a)
    b_index = list.index(b)
    dif = abs(a_index-b_index)
    if dif == 0:
        print('E')
    elif dif == 1:
        print('A')
    elif dif == 5:
        print('A')
    elif dif == 3:
        print('C')
    else:
        print('X')

T = int(input())
list = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
for i in range(1, T+1):
    a, b = map(str, input().split())

    a_index = list.index(a)
    b_index = list.index(b)
    dif = abs(a_index-b_index)
    if dif == 0:
        print('E')
    elif dif == 1 or dif == 5:
        print('A')
    elif dif == 3:
        print('C')
    else:
        print('X')

    
    
