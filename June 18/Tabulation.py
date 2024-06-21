l = [1, 2, 5]
v = 5
n = len(l)
a = [[float('inf')] * (v + 1) for _ in range(n + 1)]
for i in range(n + 1):
    a[i][0] = 0


for i in range(1, n + 1):
    for j in range(1, v + 1):
        if j < l[i - 1]:
            a[i][j] = a[i - 1][j]
        else:
            a[i][j] = min(a[i - 1][j], a[i][j - l[i - 1]] + 1)

result = a[n][v] if a[n][v] != float('inf') else -1
print(result)