def solution(files):
    tmp = []  # 파일명을 세 부분으로 나누어 저장할 임시 리스트
    head, number, tail = '', '', ''  # 각 파일명 부분을 저장할 변수들
    
    # 주어진 파일명들에 대해 반복
    for file in files:
        # 파일명을 순회하며 숫자를 만날 때까지 HEAD 부분 추출
        for i in range(len(file)):
            if file[i].isdigit():
                head = file[:i]
                number = file[i:]

                # 숫자 이후에 나오는 문자를 TAIL로 추출
                for j in range(len(number)):
                    if not number[j].isdigit():
                        tail = number[j:]
                        number = number[:j]
                        break

                # HEAD, NUMBER, TAIL을 추출하여 tmp 리스트에 추가
                tmp.append([head, number, tail])
                head, number, tail = '', '', ''
                break

    # HEAD 부분을 기준으로 사전 순 정렬하되, 대소문자를 구분하지 않음
    # NUMBER 부분을 숫자로 변환하여 순서대로 정렬
    tmp = sorted(tmp, key=lambda x: (x[0].lower(), int(x[1])))

    # 정렬된 결과를 문자열로 결합하여 반환
    return [''.join(i) for i in tmp]

# 코드 설명:

# tmp 리스트는 각 파일명을 HEAD, NUMBER, TAIL로 나누어 저장할 임시 리스트입니다.
# head, number, tail은 파일명의 각 부분을 저장할 변수들입니다.
# 파일명들에 대해 반복하면서 HEAD 부분을 추출하고, 숫자를 만나면 NUMBER와 TAIL 부분을 추출합니다.
# 추출한 HEAD, NUMBER, TAIL을 tmp 리스트에 추가합니다.
# tmp 리스트를 정렬할 때는 HEAD를 기준으로 사전 순 정렬하되, 대소문자를 구분하지 않습니다. NUMBER는 숫자로 변환하여 정렬합니다.
# 정렬된 결과를 문자열로 결합하여 반환합니다.