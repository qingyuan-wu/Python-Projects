# Completed Nov 2020
# Perform Gaussian Elimination on matrix (as 2D array) M, thus solving
# Mx = b for some unknown vector x and column vector b.

# Needed for array() and dot():
from numpy import *

# Helpers
def print_matrix(M_lol):
    M = array(M_lol)
    print(M)

def get_lead_ind(row):
    for i in range(len(row)):
        if row[i] != 0:
            return i

    return len(row)

def get_row_to_swap(M, start_i):
    prev = [start_i, get_lead_ind(M[start_i])]
    for i in range(start_i, len(M)):
        if get_lead_ind(M[i]) < get_lead_ind(M[start_i]):
            if get_lead_ind(M[i]) < prev[1]:
                prev = [i,get_lead_ind(M[i])]

    return prev[0]

def add_rows_coefs(r1, c1, r2, c2):
    sum = [0]*len(r1)
    for i in range(len(r1)):
        sum[i] = c1*r1[i] + c2*r2[i]

    return sum

def eliminate(M, row_to_sub, best_lead_ind):

    for i in range(row_to_sub + 1, len(M)):
        c1 = - (M[i][best_lead_ind] / M[row_to_sub][best_lead_ind])
        M[i] = add_rows_coefs(M[row_to_sub], c1, M[i], 1)
        for j in range(len(M[i])):
            if int(M[i][j]) == M[i][j]:
                M[i][j] = int(M[i][j])

    return M

def eliminate_rev(M, row_to_sub, best_lead_ind):
    for i in range(row_to_sub-1,-1,-1):
        c1 = - (M[i][best_lead_ind] / M[row_to_sub][best_lead_ind])
        M[i] = add_rows_coefs(M[row_to_sub], c1, M[i], 1)

    return M

def forward_step(M):
    print("The matrix is currently:")
    print_matrix(M)

    for i in range(len(M)):
        print("Now looking at row", i)

        row = get_row_to_swap(M, i)
        print("Swapping rows", i, "and", row, "so that entry", get_lead_ind(M[row]), "in the current row is non-zero")
        M[i], M[row] = M[row], M[i]
        print("The matrix is currently:")
        print_matrix(M)
        print("====================================================================")
        print("Adding row", i, "to rows below it to eliminate coefficients in column", get_lead_ind(M[i]))
        eliminate(M, i, get_lead_ind(M[i]))
        print("The matrix is currently:")
        print_matrix(M)
        print("====================================================================")
    print("Done with the forward step")
    print("The matrix is currently:")
    print_matrix(M)

def backward_step(M):
    forward_step(M)
    print("====================================================================")
    print("Now performing the backward step")

    for i in range(len(M)):
        print("Adding row", len(M)-1-i, "to rows above it to eliminate coefficients in column", get_lead_ind(M[-1-i]))
        if get_lead_ind(M[-1-i]) != len(M[-1-i]):
            eliminate_rev(M, len(M)-1-i, get_lead_ind(M[-1-i]))
        print("The matrix is currently:")
        print_matrix(M)
        print("====================================================================")

    print("Now dividing each row by the leading coefficient")
    for i in range(len(M)):
        if get_lead_ind(M[i]) != len(M[i]):

            x = M[i][get_lead_ind(M[i])]
            for j in range(len(M[0])):
                M[i][j] /= x

    print("The final matrix in RNF:")
    print_matrix(M)

# Solving Mx = b using GE
def solve(M, b):
    AUG = M
    for i in range(len(AUG)):
        AUG[i].append(b[i])

    forward_step(AUG)
    backward_step(AUG)
    print("Solutions:")
    for i in range(len(AUG)):
        print("x" + str(i+1), "=", AUG[i][-1])


if __name__ == '__main__':

    N = [[5, 6, 7, 8],
    [0,0, 1, 1],
    [0, 0, 5, 2],
    [0, 0, 7, 0]]

    M = [[0, 0, 1, 0, 2],
    [1, 0, 2, 3, 4],
    [3, 0, 4, 2, 1,],
    [1, 0, 1, 1, 2]]

    K = [[1, -2, 3, 22],
        [3, 10, 1, 314],
        [1, 5, 3, 92]]

    A = [[1,0,0],[0,1,0],[0,0,1]]
    b = [3,24,2]

    solve(A,b)