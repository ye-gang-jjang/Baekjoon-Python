# 1
import sys


n1 = int(input())
n1_list = list(map(int, input().split()))
print(min(n1_list), max(n1_list))

# 2
n2 = int(input())
n2_list = list(map(int, input().split()))
n2_list.sort()
print(n2_list[0], n2_list[-1])

# 3
input = sys.stdin.readline
n3 = input()
num3_list = list(map(int, input().split()))
n_max = num3_list[0]
n_min = num3_list[0]
for i in num3_list:
    if i > n_max:
        n_max = i
    if i < n_min:
        n_min = i
print(n_min, n_max, end='')

# 4
input = sys.stdin.readline
n4 = input()
num4_list = list(map(int, input().split()))
print(min(num4_list), max(num4_list), end='')

# shot 5
print(min(a := [*map(int, [*open(0)][1].split())]), max(a))

# 6
input()
*a, = map(int, input().split())
print(min(a), max(a))
