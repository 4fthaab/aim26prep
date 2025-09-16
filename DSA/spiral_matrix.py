n = int(input())
res = [[0 for i in range(n)] for i in range(n)]
a = 1

for layer in range((n + 1) // 2):
    # Fill top row
    for i in range(layer, n - layer):
        res[layer][i] = a
        a += 1
    # Fill right column
    for i in range(layer + 1, n - layer):
        res[i][n - layer - 1] = a
        a += 1
    # Fill bottom row
    for i in range(n - layer - 2, layer - 1, -1):
        res[n - layer - 1][i] = a
        a += 1
    # Fill left column
    for i in range(n - layer - 2, layer, -1):
        res[i][layer] = a
        a += 1

print(res)
