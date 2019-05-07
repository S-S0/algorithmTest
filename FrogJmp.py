# https://app.codility.com/programmers/lessons/3-time_complexity/
# O(1)

def solution(X, Y, D):
    if X == Y:
        return 0
    
    Y = Y - X
    STEP = Y//D
    
    if Y%D > 0:
        STEP = STEP + 1
        
    return STEP
