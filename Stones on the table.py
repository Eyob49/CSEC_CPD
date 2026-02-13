import sys
input = sys.stdin.readline

n = int(input())
stones = input().strip()
count = sum(1 for i in range(1,n) if stones[i] == stones[i-1])
print(count)
