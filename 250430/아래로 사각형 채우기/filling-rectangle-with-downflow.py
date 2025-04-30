n = int(input())
arr = [
    [0 for _ in range(n)]
    for _ in range(n)
]


# val = 1
# for i in range(n) :
#     for j in range(n) :
#         if j == 0 and i == 0 :
#            arr[i][j] = val
#         elif j == 0 :
#             val += 1
#             arr[i][j] = val 
#         else :
#             arr[i][j] = arr[i][j -1] + n

num = 1
for i in range(n):
	for j in range(n):
		arr[j][i] = num
		num += 1


for row in arr :
    for elem in row :
        print(elem,end = " ")
    print() 

