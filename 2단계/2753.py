year = int(input())

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(1)
else:
    print(0)


# 4의 배수면서 100의 배수가 아닌 년도 or 400의 배수인 년도
