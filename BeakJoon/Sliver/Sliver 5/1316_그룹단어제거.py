import sys
input = sys.stdin.readline

n = int(input())
cnt = n

for _ in range(n) :
    word = input()
    for i in range(len(word)-1) :
        if word[i] == word[i+1] :
            pass
        elif word[i] in word[i+1:] :
            cnt -= 1
            break

print(cnt)

# import sys
# from collections import Counter
#
# def func(n, w):
#     for i in range(n):
#         j = 0
#         while j < len(w[i]) - 1:
#             if w[i][j] == w[i][j+1]:
#                 w[i].pop(j)
#             else:
#                 j += 1
#     return
#
# N = int(sys.stdin.readline())
# word = [list(sys.stdin.readline().strip()) for _ in range(N)]
# func(N, word)
# cnt = 0
# 
# for i in range(N):
#     word_counter = Counter(word[i]) 
#     is_group_word = True 
#     for count in word_counter.values(): 
#         if count != 1: 
#             is_group_word = False 
#             break 
#     if is_group_word:
#         cnt += 1
# print(cnt)