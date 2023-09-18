# n = input()
n = "quackquackquackquackquackquackquackquackquackquack"
n = str(n)

right = "quack"

idx = 0

pair = 0

alright = 0

is_right = 0

duck = 0
for i in range(len(n)):
    if n[i] == right[idx]:
        alright += 1
        is_right += 1
        idx += 1
    if alright == 5:
        idx = 0
        alright = 0
        duck += 1
    if duck >= 2 and is_right == i+1:
        duck -= 1

if duck == 0:
    print(-1)
else:
    print(duck)