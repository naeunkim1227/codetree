n = 4


# for _ in range(n) :
#     arr_id = list(map(int,input().split()))
#     arr_2.push(arr_id)


arr_2 = [
    list(map(int,input().split()))
    for _ in range(n)
]


for elem in arr_2 :
    arr1 = elem
    sum_val = 0
    for i in elem :
        sum_val += i
    print(sum_val)
print()