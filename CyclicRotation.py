# https://app.codility.com/programmers/lessons/2-arrays/cyclic_rotation/

def solution(A, K):
    if not A:
        return A
    else:
        K %= len(A)
        return A[-K:] + A[:-K]
