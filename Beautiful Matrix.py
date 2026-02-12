import sys
input = sys.stdin.readline
for i in range(5):
    n = input().split()
    if '1' in n:
        c = n.index('1')
        k = i
print(abs(k - 2) + abs(c - 2))
