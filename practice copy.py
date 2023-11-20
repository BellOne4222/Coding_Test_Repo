import sys

a, p = map(int,sys.stdin.readline().split())

non_duplicate = []

non_duplicate.append(a)

while True:
    duplicate = str(non_duplicate[-1])
    compare = 0
    for i in duplicate:
        compare += int(i) ** p
    if compare in non_duplicate:
        break
    non_duplicate.append(compare)
    
print(non_duplicate.index(compare))