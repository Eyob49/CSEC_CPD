import sys
input = sys.stdin.readline

word = input().strip()
if len(set(word)) %2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
