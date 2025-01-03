import sys
import random

Q = []
A = []

################################## < Example > ##################################
Q1 = "눈이 좋은 사슴은?"
A1 = "굿아이디어"
Q.append(Q1)
A.append(A1)
#################################################################################
# Qn = "자신이 내고 싶은 문제"
# An = "해당 문제의 정답"
# Q.append(Qn)      # 문제 group에 위 문제를 추가
# A.append(An)      # 정답 group에 위 문제 정답을 추가


# 자신이 내고 싶은 퀴즈 문제 및 정답 작성
# 여러개 만들어도 좋음!
################################## < TO DO > ##################################
Q100 = "Who is best vtuber in hololive?"
A100 = "mumei"
Q.append(Q100)
A.append(A100)
#################################################################################
# 실행 방법: VScode 왼쪽 위 터미널 -> 새 커미널 -> "python 퀴즈.py" 입력

total = len(Q)
if (total < 3):
    sys.exit(1)

print("퀴즈 쇼에 오신 것을 환영합니다!!!!!")
print("아래 나오는 문제들에 알맞은 답을 입력해 주세요!\n")

already_extracted_q = []
count = 0
answer_count = 0
for i in range(3):
    count += 1
    while (1):
        rd_idx = random.randint(0, total - 1)
        if rd_idx not in already_extracted_q:
            already_extracted_q.append(rd_idx)
            break
    print(f"문제 {count}: {Q[rd_idx]}")
    player_answer = input()
    if (player_answer == A[rd_idx]):
        print("정답입니다!!\n")
        answer_count += 1
    else:
        print("아쉽지만, 틀렸습니다 ㅠㅠ")
        print(f"정답은 '{A[rd_idx]}'였습니다.\n")

print(f"총 {count} 개의 문제 중 {answer_count} 개의 문제를 맞히셨습니다.")
print("퀴즈 쇼가 끝났습니다! 수고하셨습니다!!!")