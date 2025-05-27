n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.


nums.sort()
for elem in nums : 
    print(elem,end = " ")

print()

nums.sort(reverse=True)
for elem in nums : 
    print(elem,end = " ")