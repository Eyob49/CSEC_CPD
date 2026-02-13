import sys
input = sys.stdin.readline 

n = int(input())
a = list(map(int, input().split()))
police_officers = 0
no_crimes = 0
for i in range(n):
    if a[i] == -1 and police_officers > 0:
        police_officers += a[i]
    elif a[i] > 0:
        police_officers += a[i]
    else:
        no_crimes += 1
print(no_crimes)
