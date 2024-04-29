def case_one(amountText, flag):
    for t in amountText:
        if not (t.isdigit() or t == ","):
            flag = False
            break
    return flag

def case_two(amountText, flag):
    for i in range(len(amountText)):
        if amountText[0] == "0" or amountText[0] == "," or amountText[-1] == ",":
            flag = False
            break
    return flag

def case_three(amountText, flag):
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
    return flag


def solution(amountText):
    
    # 1. 숫자 or ,

    # 2. 0원아니면 가장 왼쪽에 0 x

    # 3. 구분자 ,가 없어도 옳은 금액

    # 4. 구분자는 세자리 숫자에만 사용

    # 5. 왼쪽 끝 or 오른쪽 끝에는 구분자 x

    flag = True

    case_one(amountText, flag)

    if not flag:
        return False
    else:
        case_two(amountText, flag)       

    if not flag:
        return False
    else:
        case_three(amountText, flag) 
    
    if not flag:
        return False
    else:
        return True

print(solution("39,00"))