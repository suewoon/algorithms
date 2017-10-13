#!/usr/local/bin python3
# http://www.geeksforgeeks.org/dynamic-programming-set-8-matrix-chain-multiplication/


def matrix_chain_order(p, n):
    # m[i, j] = # of minimum multiplcations needed to compute
    # A[i]A[i+1]..A[j] where dimension of A[i] = p[i-1]p[i]
 
    m = [[float('inf') for _ in range(n)] for _ in range(n)]

    # when multiplying one matrix, cost = 0
    for i in range(1, n):
        m[i][i] = 0

    # 길이는 2부터 n-1까지 
    for L in range(2, n):
        # 길이가 L일때 시작할수 있는 i 범위 
        for i in range(1, n-L+1):
            j = i+L-1  # 시작 i, 길이 L일때 끝값 j
            # i, j 사이 k지점에 괄호가 있을 때
            for k in range(i, j): # q = cost/scalar multiplications
                q = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j]
                m[i][j] = min(q, m[i][j])

    return m[1][n-1]


arr = [1, 2, 3, 4]
size = len(arr)
print("# of minimum of multiplications is ", matrix_chain_order(arr, size))
