T = int(input())
for tc in range(1, T + 1):
    data,n= input().split()
    nums = list(data)
    N = int(n)
    for i in range(len(nums)):
        if N == 0:
            break
        max_val = nums[i]
        max_idx =-1
        for j in range(i + 1, len(nums)):  
            if nums[j] >= max_val:
                max_val = nums[j]
                max_idx = j
        if max_idx != -1 and max_val > nums[i]:
            nums[i],nums[max_idx] = nums[max_idx], nums[i]
            N -= 1
    result = "".join(nums)
    print(f"#{tc} {result}")  # 으아아아아아아아아아아ㅏㅏㅏㅏ 