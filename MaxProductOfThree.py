# https://app.codility.com/programmers/lessons/6-sorting/max_product_of_three/
# Detected time complexity: O(N * log(N))

def solution(A):
    A.sort()
    AA = A[0] * A[1] * A[len(A)-1]
    BB = A[len(A)-1]*A[len(A)-2]*A[len(A)-3]
    if AA >= BB:
        return AA
    else:
        return BB
