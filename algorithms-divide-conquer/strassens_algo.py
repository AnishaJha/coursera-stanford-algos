import math


def pad_zeros(mat1, mat2):
    n = len(mat1)
    log_n = math.log(n, 2)
    if log_n != int(log_n):
        new_len = 2 ** (int(log_n) + 1)
        for i in range(n):
            mat1[i] = mat1[i] + [0] * (new_len - n)
            mat2[i] = mat2[i] + [0] * (new_len - n)
        l = n
        while l < new_len:
            mat1.append([0] * new_len)
            mat2.append([0] * new_len)
            l = l + 1
    return mat1, mat2


def strassens_algo(mat1, mat2):
    if len(mat1) == 1:
        return [mat1[0][0] * mat2[0][0]]
    len_new = len(mat1) // 2
    A = mat1[0:len_new][0:len_new]
    B = mat1[0:len_new][len_new:]
    C = mat1[len_new:][0:len_new]
    D = mat1[len_new:][len_new:]
    E = mat2[0:len_new][0:len_new]
    F = mat2[0:len_new][len_new:]
    G = mat2[len_new:][0:len_new]
    H = mat2[len_new:][len_new:]
    [[]]



mat1, mat2 = pad_zeros([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]],
                       [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]])
