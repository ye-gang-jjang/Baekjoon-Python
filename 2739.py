n = int(input())

for i in range(9):
    print(n, "*", i+1, "=", n*(i+1))


# 1. a = b = int(input()); exec("print(a,'*',b//a,'=',b);b+=a;"*9)
