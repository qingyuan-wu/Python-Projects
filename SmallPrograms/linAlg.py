# Completed: Summer 2021
# Functions computing some basic matrix operations: addition, exponentiation, determinant

def multiply(A, B):
    '''
    Perform matrix multiplication
    A, B are 2D arrays with matching internal dimensions
    '''
    res = []
    for i in range(len(A)):
        res.append([])

    for i in range(len(A)):

        for k in range(len(B[0])):
            entry = 0
            for j in range(len(A[0])):
                entry += A[i][j] * B[j][k]
            res[i].append(entry)

    return res

def minor(A, i ,j):
    '''
    Return the i,j-th minor of A
    i-th row and j-th column removed from A
    '''
    #initialize min to be [[],[],[]...]
    min = []
    for k in range(len(A)-1): # can't use i again
        min.append([])
    count = 0 # track which row of the MINOR we're at.
    # need the row to avoid index error (minor has one less row)

    for row in range(len(A)):
        if row != i: # skip the i-th row
            for col in range(len(A[0])):
                if col != j: # skip the j-th column
                    min[count].append(A[row][col])
            count += 1

    return min

def det(A):
    '''
    Returns the determinant using the Laplace expansion formula
    Run across the first row of A
    Assume A is square
    '''
    if len(A) <= 1:
        return A[0][0]
    res = 0
    for j in range(len(A[0])):
        # recursive formula of the det using Laplace expansion
        res += A[0][j] * (-1)**j * det(minor(A,0,j))

    return res

def power(A, n):
    '''
    Computes A^n, where A is a square matrix and n a positive integer
    '''
    res = A
    for i in range(1,n):
        res = multiply(res,A)

    return res


# tests
A = [[1,0,0],
    [0,5,0],
    [0,0,9]]

B = [[12,2],
    [4,5]]

C = [[1,2,3,9],
    [11,5,6,-4],
    [7,8,12,-11],
    [8,-7,5,4]]

print(minor(A,0,0))
print(det(A))

print("-----")
print(minor(B,0,0))
print(det(B))

print("-----")
print(minor(C, 1,1))
print(det(C))