T = 10
for i in range(1, T+1):
    for a in str(i):
        result = ""
        if a == str(3) or a == str(6) or a == str(9):
            result += "-"
        else:
            result = a
    print(result, end = " ")