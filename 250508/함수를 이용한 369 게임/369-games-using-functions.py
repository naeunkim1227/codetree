a, b = map(int, input().split())

# Please write your code here.
def is_contain_number(i) :
    while i > 0 : 
        if i % 10 == 3 or i % 10 == 6 or i % 10 == 9 :
            return True
        i //= 10

    return False



count = 0
for i in range(a,b+1) :
    if i % 3 == 0 or is_contain_number(i) :
        count += 1

print(count)