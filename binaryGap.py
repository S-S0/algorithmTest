def solution(N):
    # write your code in Python 3.6
    sanitizeList = []
    binNum = bin(N).split("b")[1]
    binLen = len(binNum)
    oneCount = binNum.count("1")
    
    if oneCount < 2 | oneCount == binLen:
        return 0

    zeroSplit = binNum.split("1")
    
    if zeroSplit[-1]:
        sanitizeList = zeroSplit[:-1]
    else:
        sanitizeList = zeroSplit
        
    sanitizeList.sort(reverse=True)
    return len(sanitizeList[0])
    
    pass
