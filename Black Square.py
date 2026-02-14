import sys
input = sys.stdin.readline

cal = list(map(int, input().split()))
s = input().strip()

total = 0
for char in s:
    index = int(char) - 1
    total += cal[index]

print(total)
