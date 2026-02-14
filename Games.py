import sys
from collections import Counter

input = sys.stdin.read().split()
n = int(input[0])

home_colors = []
away_colors = []
for i in range(1, 2 * n + 1, 2):
    home_colors.append(int(input[i]))
    away_colors.append(int(input[i+1]))
home_freq = Counter(home_colors)
away_freq = Counter(away_colors)
ans = 0
for color in home_freq:
    if color in away_freq:
        ans += home_freq[color] * away_freq[color]
print(ans)
