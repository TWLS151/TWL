# BOJ - 25501
# 재귀의 귀재


def recursion(s, l, r):
    global count
    count += 1
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

# print('ABBA:', isPalindrome('ABBA'), count)
# print('ABC:', isPalindrome('ABC'), count)

tc = int(input())

for _ in range(tc):
    string = input()
    count = 0

    print(isPalindrome(string), count)