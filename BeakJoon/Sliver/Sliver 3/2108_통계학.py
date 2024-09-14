import sys
sys.stdin = open('input.txt')

from collections import Counter

N = int(sys.stdin.readline())
num  = sorted([int(sys.stdin.readline()) for _ in range(N)])

# 산술 평균
print(round(sum(num) / N))

# 중앙값
print(num[N//2])

# 최빈값
mode = Counter(num).most_common()
if len(mode) > 1:
    if mode[0][1] == mode[1][1]:
        print(mode[1][0])
    else:
        print(mode[0][0])
else:
    print(mode[0][0])

# 범위
print(num[-1]-num[0])