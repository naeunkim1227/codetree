a, b = map(int, input().split())

# Please write your code here.
def number(a,b) : 
    if a > b :
        a += 25
        d *= 2
    else :
        b += 25
        a *= 2 
    return a,b

a,b = number(a,b)
print(a,b)