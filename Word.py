import sys
input = sys.stdin.readline

s = input().strip()
upper_count = sum(1 if char == char.upper() else 0 for char in s)
lower_count = sum(1 if char == char.lower() else 0 for char in s)
print(s.upper() if upper_count > lower_count else s.lower())
