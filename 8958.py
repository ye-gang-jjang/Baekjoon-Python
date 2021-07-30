test_case = int(input())

for i in range(test_case):
    ox_list = input()
    score = 0
    sum_score = 0
    for j in ox_list:
        if j == 'O':
            score += 1
        else:
            score = 0
        sum_score += score
    print(sum_score)