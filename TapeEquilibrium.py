# https://app.codility.com/programmers/lessons/3-time_complexity/tape_equilibrium/
# Detected time complexity: O(N)

def solution(A):
    if len(A) == 2:
        return abs(A[0] - A[1])
    PreSum = A[0]
    PostSum = sum(A[1:])
    Radix = abs(PreSum - PostSum)
    for i in range(1, len(A)-1):
        PreSum += A[i]
        PostSum -= A[i]
        Tmp = abs(PreSum - PostSum)
        if Tmp < Radix:
            Radix = Tmp
    return Radix