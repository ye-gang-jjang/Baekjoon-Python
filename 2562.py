num_list = []
for numbers in range(9):
    num_list.append(int(input()))
print(max(num_list))
print(num_list.index(max(num_list))+1)


#1
# n_list = list(map(int, input().split()))
# s = 1
# n_max = n_list[0]

# for i in n_list:
#     if i > n_max:
#         n_max = i
#         s += 1
# print(n_max, s)


# 2
# a = []
# for i in range(9):
#     a.append(int(input()))
# print(max(a))
# print(a.index(max(a)+1))