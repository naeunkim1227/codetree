n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.

max_val = -1
# for curr_num in nums :
#     if max_val < curr_num :
#         count = 0 
#         for elem in nums :
#             if elem == curr_num :
#                 count+= 1
        
#         if count == 1 :
#             max_val = curr_num
  
    

    
# print(max_val)

for i in range(n) :
    cnt = nums.count(nums[i])

    if max_val < nums[i] and cnt == 1 :
        max_val = nums[i]




print(max_val)

    