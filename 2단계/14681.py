a = int(input())
b = int(input())

if a > 0:
    if b > 0:
        print("1")
    else:
        print("4")
else:
    if b > 0:
        print("2")
    if b < 0:
        print("3")

# 1. print("3421"[input()>"0"::2][input()>"0"])

# 2. a,b=open(0);print('3421'[a>'0'::2][b>'0'])

# 3. a,b=map(int,open(0))
#   print('3421'[a>0::2][b>0])
