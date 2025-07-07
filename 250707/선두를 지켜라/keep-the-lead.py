n, m = map(int, input().split())
MAX_T = 1000000
pos_a,pos_b = [0] * (MAX_T + 1),[0] * (MAX_T + 1)


time_a = 1
for _ in range(n) :
  v,t =  map(int,input().split())
  for _ in range(t):
    pos_a[time_a] = pos_a[time_a - 1] + v
    time_a += 1


time_b = 1
for _ in range(m) :
  v,t =  map(int,input().split())
  for _ in range(t):
    pos_b[time_b] = pos_b[time_b - 1] + v
    time_b += 1


leader,ans = 0,0

for i in range(1,time_a) : 
  if pos_a[i] > pos_b[i] :
    if leader == 2:
      ans += 1

    leader = 1

  elif pos_a[i] < pos_b[i] :
    if leader == 1 :
      ans += 1
    leader =2


print(ans)



