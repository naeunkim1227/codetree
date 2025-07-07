n, m, k = tuple(map(int, input().split()))
penalized_person = [
    int(input())
    for _ in range(m)
]
penalty_num = [0] * (n + 1)

ans = -1
for target in penalized_person:
    penalty_num[target] += 1

    if penalty_num[target] >= k:
        ans = target
        break

print(ans)
