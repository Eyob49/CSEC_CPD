import sys
input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))

left = 0
right = n - 1
s = 0
d = 0


turn = 0

while left <= right:
    
    if cards[left] > cards[right]:
        chosen_card = cards[left]
        left += 1
    else:
        chosen_card = cards[right]
        right -= 1
    
     
    if turn % 2 == 0:
        s += chosen_card
    else:
        d += chosen_card
    
    turn += 1
print(s,d)
