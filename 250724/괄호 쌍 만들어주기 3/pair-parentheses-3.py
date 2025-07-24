A = input()
n = len(A)


cnt = 0
# Please write your code here.
for i in range(n) :
    for j in range(i+1,n) :
        if A[i] == '(' and A[j] == ')' :
            cnt+= 1


print(cnt)
