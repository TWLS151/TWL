N = int(input())
L = list(map(int,input().split()))
min_long = 1
max_long = 1
longest = 0
for i in range(N-1): #돌면서 가장 긴 줄어드는 or 증가하는 수열을 찾으면 된가 이거 아님?(나랑 다음꺼 까지 고민하기 때문에 N-1까지만 탐색)
    #일단 숫자가 커지는 경우를 생각해보자고.
    if L[i]< L[i+1]:
        #큰 경우 작은애는 초기화 
        # 그리고 크기는 추가 
        longest = max(min_long,longest)
        max_long+=1
        min_long =1
    elif L[i]==L[i+1]:
        max_long+=1
        min_long +=1
    else:
        min_long+=1
        longest = max(longest,max_long)
        max_long = 1
        
longest = max(max_long,longest,min_long)
print(longest)