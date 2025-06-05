a, b, c = map(int, input().split())

# Please write your code here.

def calc_min (a,b,c) :
    return (60 * b) + (60 * 24 * a) + c



print(calc_min(a,b,c) - calc_min(11,11,11))