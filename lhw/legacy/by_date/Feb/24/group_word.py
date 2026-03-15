# BOJ - 1316
# 그룹 단어 체커
# 구현

def checker(word):

    if len(word) == 1:
        return 1

    run = 0
    for i in range(1, len(word)):
        # if i + 1 < len(word):
        if word[i] == word[i-1]:
            # run += 1
            continue
        # else:
            run = 0
            
        if word[i] in word[:i]:
            return 0
    return 1



N = int(input())
count = 0

for _ in range(N):
    word = input()
    history = set()

    count += checker(word)

print(count)
