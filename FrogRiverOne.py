# https://app.codility.com/programmers/lessons/4-counting_elements/frog_river_one/
# Detected time complexity: O(N)

def solution(X, A):
    leaves = {}
    cnt = 0
    for i in A:
        if i <= X:
            leaves[i] = ""
        if len(leaves) == X:
            return cnt
            break
        cnt += 1
    return -1
