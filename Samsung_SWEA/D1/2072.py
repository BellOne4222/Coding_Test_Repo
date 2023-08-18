# 2078 홀수만 더하기

T = int(input())
 
for test_case in range(1,T+1):
    evens = map(int, input().split())
    even = []
    for i in evens:
        if i%2 !=0:
            even.append(i)
    answer = sum(even)
    print("#"+str(test_case),answer)

# t = int(input())
 
# for test_case in range(1,t+1):
#     li = map(int, input().split())
#     answer = 0
#     for i in li:
#         if i%2!=0:
#             answer += i
#     print("#"+str(test_case),str(answer))