memo = {1:1, 2:2}
i = 3

for i in range(3, 4000000):
    memo[i] = memo[i - 1] + memo[i - 2]
    if memo[i] > 4000000:
        break
    
print(sum(val for val in memo.values() if val % 2 == 0))
