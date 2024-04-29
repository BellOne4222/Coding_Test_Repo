amountText = "39,00"
flag = True

cnt = 0
for j in reversed(range(len(amountText))):
    if amountText[j] == ",":
        if cnt != 3:
            flag = False
            break
        else:
            cnt = 0
    else:
        cnt += 1

print(flag)