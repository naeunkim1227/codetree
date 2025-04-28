m,n = 2,4

arr_2d = [
    list(map(int,input().split()))
    for _ in range(2)
]


garo = []
sero = []
total = 0 
idx = 0
garoTotal= 0

# 가로
for i in range(2):
	sum_val = 0
	for j in range(4):
		sum_val += arr_2d[i][j]
	print(f"{sum_val / 4:.1f}", end=" ")
print()



# 세로
for j in range(4):
	sum_val = 0
	for i in range(2):
		sum_val += arr_2d[i][j]
	print(f"{sum_val / 2:.1f}", end=" ")
print()


# 전체
for i in range(m) :
    for j in range(n) :
          total += arr_2d[i][j]
          idx+= 1

print(f"{total/idx:.1f}")