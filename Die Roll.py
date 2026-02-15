import sys
input = sys.stdin.readline
from fractions import Fraction

y,w = map(int, input().split())
a = max(y,w)
d = (6 - a) + 1
ans = Fraction(d, 6)
print(str(ans.numerator) + '/' + str(ans.denominator))
