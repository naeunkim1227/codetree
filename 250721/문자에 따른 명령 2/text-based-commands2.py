dirs = input()

# Please write your code here.
x,y = 0,0
curr_dir = 3
dx,dy = [1,0,-1,0],[0,-1,0,1]


for c_dir in dirs :
    if c_dir == 'L' :
        curr_dir = (curr_dir -1 + 4) % 4
    elif c_dir == 'R' :
        curr_dir = (curr_dir + 1 ) % 4
    else :
        x,y = x + dx[curr_dir], y + dy[curr_dir]


print(x,y)