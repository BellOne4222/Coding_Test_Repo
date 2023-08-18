def check_gear_shift_order(shifts):
    # 변속 순서의 첫 번째와 마지막 숫자를 가져옴
    first_shift = shifts[0]
    last_shift = shifts[-1]
    # 첫 번째 숫자가 1이고, 마지막 숫자가 8인 경우 ascending 판별
    if first_shift == 1 and last_shift == 8:
        # 변속 순서가 1에서 8로 연속적으로 증가함
        for i in range(len(shifts) - 1):
            if shifts[i] >= shifts[i + 1]:
                return "mixed"
        return "ascending"

    # 첫 번째 숫자가 8이고, 마지막 숫자가 1인 경우 descending 판별
    if first_shift == 8 and last_shift == 1:
        # 변속 순서가 8에서 1로 연속적으로 감소함
        for i in range(len(shifts) - 1):
            if shifts[i] <= shifts[i + 1]:
                return "mixed"
        return "descending"

    # 위 조건에 해당하지 않는 경우 mixed 판별
    return "mixed"


shifts = list(map(int, input().split()))
result = check_gear_shift_order(shifts)
print(result)