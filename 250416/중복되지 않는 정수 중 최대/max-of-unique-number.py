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
dup_arr = []

for i in range(n) :
    for elem in nums :
      count = 0 
      if elem == nums[i] :
          count+= 1

if count > 1 :
        dup_arr.append(nums[i])


print(dup_arr)

    