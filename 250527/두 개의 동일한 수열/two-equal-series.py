n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.
A.sort()
B.sort()

tf = "Yes"
for i in range(n) : 
    if A[i] != B[i] : 
        tf = "No"

print(tf)