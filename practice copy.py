n = int(input())
towers = list(map(int, input().split()))
stack = []
result = [0 for i in range(n)]
 
for i in range(n):
    while stack:
        if stack[-1][1] > towers[i]:
            result[i] = stack[-1][0] + 1
            break
        else:
            stack.pop()
    stack.append([i, towers[i]])
 
print(" ".join(map(str,result)))
