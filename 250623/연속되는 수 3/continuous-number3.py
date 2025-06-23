N = int(input())
arr = [int(input()) for _ in range(N)]

# Please write your code here.

cnt,max_cnt = 0,0
for i in range(N) :
    if i >= 0 and (arr[i] * arr[i-1]> 0) :
        cnt += 1    
    else :
        cnt = 1

    max_cnt = max(max_cnt,cnt)


print(max_cnt)