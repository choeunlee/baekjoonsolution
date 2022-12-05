inf = float('inf')

city = int(input())
bus = int(input())
adj = [[inf] * city for _ in range(city)]

for _ in range(bus):
    start, finish, cost = map(int, input().split())
    adj[start-1][finish-1] = min(adj[start-1][finish-1], cost)

for k in range(city):
    for i in range(city):
        for j in range(city):
            if i == j:
                adj[i][j] = 0
            else:
                adj[i][j] = min(adj[i][j], adj[i][k] + adj[k][j])

for i in range(city):
    for j in range(city):
        if adj[i][j] == inf:
            adj[i][j] = 0
        print(adj[i][j], end=" ")
    print()
