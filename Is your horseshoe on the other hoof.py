import sys
input = sys.stdin.readline

arr = list(map(int, input().split()))
n = len(arr)
arr.sort()
count = sum(1 for i in range(1, n) if arr[i] == arr[i - 1])
print(count)
