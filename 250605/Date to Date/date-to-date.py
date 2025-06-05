m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.
num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def calData(month,day) : 
    m = month - 1
    n = 0
    for i in range(m) :
       n += num_of_days[i] 
    
    return n + day



print(calData(m2,d2)- calData(m1,d1))
