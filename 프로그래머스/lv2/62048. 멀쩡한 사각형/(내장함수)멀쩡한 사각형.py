import math

def minus_square(w,h):
    minus = w + h - math.gcd(w, h)
    return minus

def solution(w,h):
    all_square = w * h
    result = all_square - minus_square(w,h)
    return result