#1
C = int(input())
for i in range(C):
    N = list(map(int, input().split(' ')))
    avg = sum(N[1:]) / N[0]
    cnt = 0
    for j in N[1:]:
        if j > avg:
            cnt += 1

    print(str("%.3f" % round((cnt/N[0])*100, 3))+"%")


#2
n = int(input())
for _ in range(n):
    nums = list(map(int, input().split()))
    avg = sum(nums[1:])/nums[0]  # 평균을 구함 (nums[0]: 학생수, nums[1:] 점수)
    cnt = 0
    for score in nums[1:]:
        if score > avg:
            cnt += 1  # 평균 이상인 학생 수
    rate = cnt/nums[0] * 100
    print(f'{rate:.3f}%')   # f-string  f'문자열{변수}'
