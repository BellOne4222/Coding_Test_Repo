def gcd(w, h):
    if w % h == 0:
        return h
    elif h == 0:
        return w
    else:
        return gcd(h, w % h)

def minus_square(w,h):
    minus = w + h - gcd(w,h)
    return minus

def solution(w,h):
    all_square = w * h
    result = all_square - (minus_square(w,h))
    return result