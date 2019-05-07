# https://app.codility.com/programmers/lessons/3-time_complexity/perm_missing_elem/
# Detected time complexity: O(N) or O(N * log(N))

def solution(A):
    N = len(A) + 1
    SUM = int(N*(N+1)/2)
    
    for i in A:
        SUM = SUM - i
    
    if SUM == 0:
        return N
        
    return SUM
