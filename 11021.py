t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    ans = a+b
    print("Case #%s: %s" % (i+1, ans))

# (%s:문자열 %d:정수 %f:부동소수점)
