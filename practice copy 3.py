import sys
code = [0] #인덱스 값 맞추기용 0 초기값
code += list(sys.stdin.readline())
code.pop() #'\n'날리기

if code[1] == '0': 
    print(0)
    exit(0)

length = len(code)
dp = [0] * length
dp[0] = dp[1] = 1

for i in range(2, length):
    first = int(code[i])
    tenth = int(code[i-1])*10 + int(code[i])
    if first > 0: dp[i] += dp[i-1]
    if tenth >= 10 and tenth <= 26: dp[i] += dp[i-2]

print(dp[length-1]%1000000)