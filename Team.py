import sys
input = sys.stdin.readline

t = int(input())
count = 0
for _ in range(t):
    a = list(map(int, input().split()))
    if sum(a) >= 2:
        count += 1
print(count)
