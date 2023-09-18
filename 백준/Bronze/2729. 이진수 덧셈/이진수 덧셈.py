# int(value, base)
# bin() -> 2진수로 변환, 앞에 0b가 붙으므로 print 할때는 잘라야한다.

n = int(input())

for i in range(n):
    a,b = input().split(" ")
    a = int(a,2)
    b = int(b,2)
    result = bin(a+b)
    print(result[2:])