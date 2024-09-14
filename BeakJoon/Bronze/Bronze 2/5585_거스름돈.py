import sys
sys.stdin = open('input.txt')

change = 1000 - int(sys.stdin.readline())
money = [500, 100, 50, 10, 5, 1]

cnt = 0
for i in money:
    cnt += change // i
    change %= i

print(cnt)