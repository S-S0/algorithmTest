# https://app.codility.com/programmers/lessons/6-sorting/distinct/
# Detected time complexity: O(N*log(N)) or O(N)

def solution(A):
    A = list(set(A))
    return len(A)
