import sys
input = sys.stdin.readline

s = input().strip()
t = input().strip()
steps = 0
for i in range(len(t)):
    if t[i] == s[steps]:
        steps += 1
print(steps + 1)   
