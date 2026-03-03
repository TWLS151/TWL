T = int(input())
for tc in range(1, T + 1):
    str1 = input()
    str2 = input()
    max_count = 0
    for i in range(len(str1)):
        count = 0
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                count += 1
        if max_count < count:
            max_count = count
    print(f'#{tc} {max_count}')