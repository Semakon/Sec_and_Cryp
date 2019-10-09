import numpy as np


def init_matrix(c):
    l = len(c)
    M = np.array([np.zeros(l)] * (l - 1))
    for i in range(l - 1):
        M[i][i + 1] = 1
    return np.append(M, [np.flip(c)], 0)


def LFSR(M, s):
    v = np.zeros(len(s))
    v[0] = 1
    outs = np.array([])
    for i in range(20):
        new_s = np.mod(M.dot(s), 2)
        out = v.dot(s)
        # print(i, "\t-\tstate:", s, "->", new_s)
        # print("\t\tout:", out)
        # print()
        outs = np.append(outs, out)
        s = new_s
    return outs


if __name__ == "__main__":
    c = np.array([0, 1, 1, 0, 1, 0, 0, 1, 1])
    s = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1])
    M = init_matrix(c)

    print(LFSR(M, s))
