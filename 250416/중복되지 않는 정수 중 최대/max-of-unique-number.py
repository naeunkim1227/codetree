n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.

dup_arr = []
max_val = nums[0]
for i in range(1,n) :
    if nums[i] not in dup_arr and max_val < nums[i] :
        max_val = nums[i]
    elif nums[i] in dup_arr :
        max_val = -1    
    
    dup_arr.append(nums[i])


print(max_val)
     