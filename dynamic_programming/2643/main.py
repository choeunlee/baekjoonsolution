import sys

n = int(sys.stdin.readline())
paper = []

for i in range(n):
    size = sorted(list(map(int, sys.stdin.readline().split())))
    paper.append(size)
paper.sort()

output = [1 for i in range(n)]

for i in range(1, n):
    for j in range(i):
        if paper[i][1] >= paper[j][1]: 
            output[i] = max(output[i], output[j]+1)
print(max(output))
