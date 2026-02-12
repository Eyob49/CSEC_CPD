import sys
input = sys.stdin.readline

t = int(input())
n = input().strip()
anton = 0
danik = 0
for char in n:
    if char == 'A':
        anton += 1
    else:
        danik += 1
if anton > danik:
    print("Anton")
elif danik > anton:
    print("Danik")
else:
    print("Friendship")
