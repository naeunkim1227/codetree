arr = list(map(int,input().split()))


new_arr = []
for elem in arr :
    if elem == 999 or elem == -999 :
        break
    else :
        new_arr.append(elem)


print(max(new_arr), min(new_arr))