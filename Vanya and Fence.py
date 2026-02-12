import sys
input = sys.stdin.readline

number_of_friends , height_of_fence = map(int, input().split())
height_of_each_person = list(map(int, input().split()))

min_width_of_road = sum(1 if height <= height_of_fence  else 2 for height in height_of_each_person)
print(min_width_of_road)
