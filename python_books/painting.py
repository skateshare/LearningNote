


def painting(n, k):
    if n == 0:
        return 0
    if n == 1:
        return k
    if n == 2:
        return k*k
    return (k-1)*(painting(n-1, k) + painting(n-2, k))



print(painting(4,2))
