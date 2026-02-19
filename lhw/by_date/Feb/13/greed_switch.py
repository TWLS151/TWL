# BOJ - 12927
# 배수 스위치

# 뒤부터 해야하나?
# 앞부터 해야지

string = [0]
string += list(input())
count = 0
for i in range(1, len(string)):
    if string[i] == 'Y':
        count += 1
        for j in range(i, len(string), i):
            if string[j] == 'Y':
                string[j] = 'N'
            else:
                string[j] = 'Y'
print(count)
    