# https://app.codility.com/programmers/lessons/2-arrays/odd_occurrences_in_array/
# Detected time complexity: O(N) or O(N*log(N))

def solution(A):
    num = 0
    for i in A:
        num ^= i
    return num
