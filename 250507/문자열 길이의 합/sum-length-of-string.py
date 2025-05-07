n = int(input())

arr = [input() for _ in range(n)]



length = 0
acnt = 0
for i in range(n) :
     length += len(arr[i])
     if arr[i][0] == 'a' :
        acnt += 1


print(length, acnt)
