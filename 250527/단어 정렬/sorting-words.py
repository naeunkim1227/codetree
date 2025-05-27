n = int(input())
word = [input() for _ in range(n)]

# Please write your code here.

word.sort()
for elem in word : 
    print(elem)