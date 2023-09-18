n = input()

# 8진수를 10진수로 변환
eight_to_ten = int(n,8)

ten_to_two = bin(eight_to_ten)

print(ten_to_two[2:])

