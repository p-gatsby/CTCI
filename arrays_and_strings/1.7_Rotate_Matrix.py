# The runtime of this algorithm is O(n^2), where n is the number of rows (or columns) in
# the given nxn matrix. This complexity arises from the need to visit each element in
# the matrix at least once, first to transpose the matrix and then to reverse each row,
# with each operation requiring a nested loop structure that iterates through all the elements.

def rotate_matrix(m):
    N = len(m)  # the size of the matrix NxN

    for i in range(N):
        for j in range(i, N):
            m[i][j], m[j][i] = m[j][i], m[i][j]

    for i in range(N):
        j = 0
        k = N - 1
        while j < k:
            m[i][j], m[i][k] = m[j][k], m[i][j]
            j += 1
            k -= 1

    return m


def print_matrix(m):
    for i in m:
        print(i)


print_matrix(rotate_matrix([[1, 2, 3],
                            [4, 5, 6],
                            [7, 8, 9]]))
