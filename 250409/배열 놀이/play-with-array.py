n,q = tuple(map(int,input().split()))
arr = list(map(int,input().split()))

for _ in range(q) :
    quest = list(map(int,input().split()))
    
    if quest[0] == 1 :
        a = quest[1]
        print(arr[a - 1])
    elif quest[0] == 2 :
        if quest[1] in arr :
            print(arr.index(quest[1]) + 1)
        else :
            print(0)
    
    else :
        for i in range(quest[1] - 1,quest[2]) :
            print(arr[i],end =" ")
        print()