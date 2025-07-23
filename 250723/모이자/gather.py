import sys

n = int(input())
A = list(map(int, input().split()))

# Please write your code here.

min_distance = sys.maxsize;
for i in range(n) :
    distance = 0 
    for j in range(n) : 
        distance +=  abs(j-i) * A[j] 
    min_distance = min(min_distance,distance)

print(min_distance)
