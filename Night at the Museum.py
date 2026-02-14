import sys
input = sys.stdin.readline

s = input().strip()
c = 'a'
total_m = 0
    
for char in s:
        diff = abs(ord(char) - ord(c))
        moves = min(diff, 26 - diff)
        total_m += moves
        c = char
        
print(total_m)
