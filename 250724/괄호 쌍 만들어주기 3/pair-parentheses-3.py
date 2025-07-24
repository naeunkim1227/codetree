A = input()
cnt = 0

# Please write your code here.
for i in range(len(A)) :
    for j in range(i+1,len(A)) :
        if A[i] == '(' and A[j] == ')' :
            cnt+= 1


print(cnt)
