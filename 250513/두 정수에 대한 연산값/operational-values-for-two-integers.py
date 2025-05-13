a, b = map(int, input().split())

# Please write your code here.

def ab(a,b) : 
    c = a
    d = b
    if a > b :
        c = a+25
        d = b*2
    else :
        d = b+25
        c = a*2 
    print(c, d)



ab(a,b)