def solution(A,B):
    A = sorted(A)
    B = sorted(B, reverse = True)
    
    result = 0
    for i in range(len(A)):
        result += A[i] * B[i]
    
    return result
        