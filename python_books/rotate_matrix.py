

def rotate_matrix(target):
    L = len(target)
    for r in range(L):
        for c in range(r+1):
            target[r][c], target[c][r] = target[c][r], target[r][c]
    for t in range(L):
        target[t].reverse()
    return target


if __name__ == "__main__":
    matrix = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    print(rotate_matrix(matrix))

    """
    [1,4,7]
    [2,5,8]
    [3,6,9]

    idea :
    [7,4,1]
    [8,5,2]
    [9,6,3]

    [3.2,1]
    [6,5,4]
    [9,8,7]

    """