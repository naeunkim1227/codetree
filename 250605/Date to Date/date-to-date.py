# m1, d1, m2, d2 = map(int, input().split())

# # Please write your code here.
# num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


# def calData(month,day) : 
#     m = month - 1
#     n = 0
#     for i in range(m) :
#        n += num_of_days[i] 
    
#     return n + day

# print(calData(m2,d2)- calData(m1,d1))


# 변수 선언 및 입력
m1, d1, m2, d2 = tuple(map(int, input().split()))


def num_of_days(m, d):
    # 계산 편의를 위해 월마다 몇 일이 있는지를 적어줍니다. 
    days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total_days = 0
    
    # 1월부터 (m - 1)월 까지는 전부 꽉 채워져 있습니다.
    for i in range(1, m):
        total_days += days[i]
    
    # m월의 경우에는 정확이 d일만 있습니다.
    total_days += d
    
    return total_days    


# 출력
total_days = num_of_days(m2, d2) - num_of_days(m1, d1) + 1
print(total_days)
