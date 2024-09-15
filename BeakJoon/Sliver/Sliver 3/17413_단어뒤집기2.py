import sys
sys.stdin = open('input.txt')

# 입력 받기
S = sys.stdin.readline()

switch = []  # 뒤집을 단어를 임시 저장할 리스트
answer = []  # 최종 결과를 저장할 리스트
ck = 0  # 태그 안에 있는지 여부를 체크하는 플래그 (0: 태그 밖, 1: 태그 안)

for i in range(len(S)):
    if ck == 0:  # 태그 밖에 있을 때
        if S[i] == '<' or S[i] == ' ':
            if S[i] == '<':
                ck = 1  # 태그 시작을 만나면 플래그를 1로 변경
            answer += switch[::-1]  # 현재까지 모은 단어를 뒤집어서 결과에 추가
            switch = []  # 임시 저장 리스트 초기화
            answer += S[i]  # 현재 문자('<' 또는 공백)를 결과에 추가
        else:
            switch.append(S[i])  # 일반 문자는 임시 저장 리스트에 추가
    elif ck == 1:  # 태그 안에 있을 때
        if S[i] == '>':
            ck = 0  # 태그 끝을 만나면 플래그를 0으로 변경
        answer.append(S[i])  # 태그 내부 문자는 그대로 결과에 추가

# 마지막으로 남은 단어가 있다면 뒤집어서 추가
if switch:
    answer += switch[::-1]

# 결과 출력
for i in range(len(answer)):
    print(answer[i], end='')