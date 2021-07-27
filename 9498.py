n = int(input())

if 90 <= n <= 100:
    print('A')
elif 80 <= n < 90:
    print('B')
elif 70 <= n < 80:
    print('C')
elif 60 <= n < 70:
    print('D')
else:
    print('F')

# 1. print('FFFFFFDCBAA'[int(input())//10])
#           0~9, 10~19, 20~29 ... 90~99, 100
# 문자열에서 입력 받은 점수를 10으로 나눈 몫에 해당하는 문자를 출력하는 방식.
# ex) 65를 입력받으면 10으로 나눈 몫이 6이 되므로, 일곱 번째 문자인 D가 출력.
