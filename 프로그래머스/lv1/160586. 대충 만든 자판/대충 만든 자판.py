def solution(keymap, targets):
    min_enter = dict()
    for key in keymap:
        for idx, alphabet in enumerate(key):
            if alphabet in min_enter.keys():
                if idx+1 < min_enter[alphabet]:
                    min_enter[alphabet] = idx + 1
            else:
                min_enter[alphabet] = idx + 1
    
    result = []
    for target in targets:
        total_enter = 0
        for alpha in target:
            if alpha in min_enter:
                total_enter += min_enter[alpha]
            else:
                total_enter = -1
                break
        result.append(total_enter)
    return result

