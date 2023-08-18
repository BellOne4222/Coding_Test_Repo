# 2019 더블더블

T = int(input())
sum = 1
answer = []
answer.append(sum)
for i in range(1, T + 1):
    sum *= 2
    answer.append(sum)
str = ' '.join(map(str, answer))
print(str)