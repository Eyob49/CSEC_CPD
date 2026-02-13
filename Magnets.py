import sys
input = sys.stdin.readline

n = int(input())
count = 0
prev = ""
for i in range(n):
    chars = input().strip()
    if chars != prev:
        count += 1
        prev = chars
print(count)
