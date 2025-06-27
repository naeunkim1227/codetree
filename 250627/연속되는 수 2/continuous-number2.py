n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.


cnt = 0
arr_cnt = 1
blocks = []
for i in range(n):
    if i == 0 or arr[i] != arr[i-1] :
        cnt += 1
        blocks.append(arr_cnt)
    else :
        arr_cnt += 1


    


print(max(blocks))