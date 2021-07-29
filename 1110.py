
n = int(input())
num = n
circle = 0

while True:
    a = n//10
    b = n % 10
    c = (a+b) % 10
    n = (b*10)+c

    circle = circle+1
    if(num == n):
        break
print(circle)
