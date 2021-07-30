arr = []
for i in range(10):
    n = int(input())
    arr.append(n % 42)
s = set(arr)  # 중복요소 제거
print(len(s))

"""
숏코딩
#1
print(len({int(i)%42for i in open(0)}))

#2
print(len({int(input())%42 for _ in '-'*10}))

#3
print(len({*eval('int(input())%42,'*10)}))

#4
print(len({int(input())%42 for _ in range(10)}))
"""
