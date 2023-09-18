#--------------------------- 진법 문제 풀이 방법 공부 ---------------------------#
## 2진수 : 0b
## 8진수 : 0o
## 16진수 : 0x

## 10진수 => 2진수, 8진수, 16진수 변환 
value = 10

b = bin(value) # 0b1010
o = oct(value) # 0o12
h = hex(value) # 0xa

print(b)
print(o)
print(h)

## 2진수 => 10진수 변환 
a2 = int(b,2) # 10
a8 = int(o,8) # 10
a16 = int(b,16) # 10

n = input()

# 8진수를 10진수로 변환
eight_to_ten = int(n,8)

ten_to_two = bin(eight_to_ten)

print(ten_to_two[2:])

