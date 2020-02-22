

def multiplyMatrix(A, B):
    if(len(A[0])!=len(B)):
        return 0
    ans = [[0]*len(B[0]) for i in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(A[0])):
                ans[i][j] += A[i][k]*B[k][j]
    return ans

if __name__ == '__main__':
    print(multiplyMatrix([[1, 1], [1, 0]], [[13, 8], [8, 5]]))
