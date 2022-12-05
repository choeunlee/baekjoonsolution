# Authored by : ravenclaw

import sys

n = int(sys.stdin.readline())
words = [sys.stdin.readline().rstrip() for i in range(n)]
alpha_dict = {}

for word in words:
    p = len(word) - 1
    for alpha in word:
        if alpha in alpha_dict:
            alpha_dict[alpha] += pow(10, p)
        else:
            alpha_dict[alpha] = pow(10, p)
        p -= 1

alpha_dict = sorted(alpha_dict.values(), reverse = True)

output = 0
exponent = 9
for i in alpha_dict: 
    output += exponent * i
    exponent -= 1

print(output)
