h, m = map(int, input().split())

if m > 44:              # 10h 45m
    print(h, m-45)  # 10h 0m
elif m < 45 and h > 0:  # 23h 40m
    print(h-1, m+15)  # 22h 55m
else:  # 0h 30m
    print(23, m+15)  # 23h 45m


# 1. h,m=map(int,input().split())
#   print((h-(m<45))%24,(m-45)%60)
