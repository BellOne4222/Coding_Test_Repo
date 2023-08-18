def solution(s):
    arr = s.split(" ") # 공백 기준으로 문자열 분리
    for i in range(len(arr)):
        arr[i] = arr[i][:1].upper() + arr[i][1:].lower() # 첫번째 글자는 대문자, 두 번째 글자는 소문자로 변환
    
    result = " ".join(arr) # 공백을 기준으로 문자열 합쳐서 반환
    return result
    
    