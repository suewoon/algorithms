def lis(idx) :
    """
    :param idx: starting index of sequence
    :return: length of longest increasing sequence which starts from idx
    """
    if cache[idx] != -1 :
        return cache[idx]
    ans = 1
    for i in range(idx,length):
        if(seq[idx]<seq[i]):
            ans = max(ans, lis(i)+1)
            # list(idx+1) + 1 : plus one in order to get a length including current one
    cache[idx] = ans
    return ans

testcases = int(input())
for i in range(testcases):
    length = int(input())
    seq = [int(j) for j in input().split()]
    cache = [-1]*length
    ans = 0
    for x in range(0,length):
        ans = max(ans,lis(x))
    print(ans)
    #print(cache)