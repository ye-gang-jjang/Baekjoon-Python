subject = int(input())  # 과목 수
test_list = list(map(int, input().split()))  # 시험점수 입력받기, list자료형
max_score = max(test_list)  # 최대값 max함수 이용

new_list = []  # 빈 리스트 생성
for score in subject:  # 입력받은 과목수 갯수만큼 돌아감
    new_list.append(score/max_score * 100)  # (입력받은 점수/최고점수*100) 새로운 점수 생성
test_avg = sum(new_list)/subject  # sum으로 모두 더하고 과목 수 만큼 나눔
print(test_avg)
