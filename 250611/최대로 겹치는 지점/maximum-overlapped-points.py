n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.

offset = 100
max_n = 200

blocks = [0] * max_n


    
for a,b in segments : 
    a,b = a + offset, b + offset
    for i in range(a,b+1) :
        blocks[i] += 1




print(max(blocks))