import numpy as np

# (m * n) * (n * p) = (m * p)Matrix
# a 1 * 3 matrix and 3 * 1 matrix is a 1 * 1 matrix
A = np.array(([1, 2],
              [3, 4]))
B = np.array(([2, 0],
              [1, 2]))
C = np.array(([1, 2, 3],
              [4, 5, 6]))
D = np.array(([7, 9, 11],
              [8, 10, 12]))


def matricesAB3():
    first = (C[0, 0] * D[0, 0]) + (C[0, 1] * D[0, 1]) + (C[0, 2] * D[0, 2])
    second = (C[0, 0] * D[1, 0]) + (C[0, 1] * D[1, 1]) + (C[0, 2] * D[1, 2])
    third = (C[1, 0] * D[0, 0]) + (C[1, 1] * D[0, 1]) + (C[1, 2] * D[0, 2])
    fourth = (C[1, 0] * D[1, 0]) + (C[1, 1] * D[1, 1]) + (C[1, 2] * D[1, 2])
    ans = np.array(([first, second], [third, fourth]))
    print(ans)


def matricesBA3():
    first = (D[0, 0] * C[0, 0]) + (D[0, 1] * C[0, 1]) + (D[0, 2] * C[0, 2])
    second = (D[0, 0] * C[1, 0]) + (D[0, 1] * C[1, 1]) + (D[0, 2] * C[1, 2])
    third = (D[1, 0] * C[0, 0]) + (D[1, 1] * C[0, 1]) + (D[1, 2] * C[0, 2])
    fourth = (D[1, 0] * C[1, 0]) + (D[1, 1] * C[1, 1]) + (D[1, 2] * C[1, 2])
    ans = np.array(([first, second], [third, fourth]))
    print(ans)


def matricesAB():
    first = (A[0, 0] * B[0, 0]) + (A[0, 1] * B[1, 0])
    second = (A[0, 0] * B[0, 1]) + (A[0, 1] * B[1, 1])
    third = (A[1, 0] * B[0, 0]) + (A[1, 1] * B[1, 0])
    fourth = (A[1, 0] * B[0, 1]) + (A[1, 1] * B[1, 1])
    ans = np.array(([first, second], [third, fourth]))
    print(ans)


def matricesBA():
    first = (B[0, 0] * A[0, 0]) + (B[0, 1] * A[1, 0])
    second = (B[0, 0] * A[0, 1]) + (B[0, 1] * A[1, 1])
    third = (B[1, 0] * A[0, 0]) + (B[1, 1] * A[1, 0])
    fourth = (B[1, 0] * A[0, 1]) + (B[1, 1] * A[1, 1])
    ans = np.array(([first, second], [third, fourth]))
    print(ans)


matricesAB()
matricesBA()
matricesAB3()
matricesBA3()
