def check(arr):
    n = len(arr)
    ans = 1

    for i in range(n):
        cnt = 1
        for j in range(1,n):
           if arr[i][j] == arr[i][j-1]:
               cnt += 1
           else:
               cnt = 1
           if cnt > ans:
               ans = cnt

        cnt = 1
        for j in range(1,n):
            if arr[j][i] == arr[j-1][i]:
                cnt += 1
            else:
                cnt = 1
            if cnt > ans:
                ans = cnt
    return ans

n = int(input())
arr = [list(input()) for _ in range(n)]
answer = 0

for i in range(n):
    for j in range(1, n):
        arr[i][j], arr[i][j-1] = arr[i][j-1], arr[i][j]
        if answer < check(arr):
            answer = check(arr)
        arr[i][j], arr[i][j-1] = arr[i][j-1], arr[i][j]

    for j in range(1, n-1):
        arr[j][i], arr[j-1][i] = arr[j-1][i], arr[j][i]
        if answer < check(arr):
            answer = check(arr)
        arr[j][i], arr[j-1][i] = arr[j-1][i], arr[j][i]

print(answer)