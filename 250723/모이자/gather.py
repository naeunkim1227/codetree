# import sys

n = int(input())
A = list(map(int, input().split()))

# Please write your code here.

max_distance = 0;
for i in range(n) :
    distance = 0 
    for j in range(n) : 
        distance +=  abs(i - j) * A[j] 
        max_distance = max(max_distance,distance)


print(max_distance)
