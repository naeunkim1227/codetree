n = int(input())
a = list(map(int, input().split()))

# Please write your code here.

min_val = a[0]
cnt = 0
for elem in a[1:] :
    if min_val > elem :
        min_val = elem
        cnt = 1
    elif min_val == elem :
        cnt += 1

print(min_val, cnt)