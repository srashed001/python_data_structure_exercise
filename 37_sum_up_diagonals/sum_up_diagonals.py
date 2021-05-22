
m1 = [[1,   2],[30, 40],]
m2 = [[1, 2, 3],[4, 5, 6],[7, 8, 9],]



def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    Tl = 0
    Tr = 0
    matrix_len = len(matrix)

    idx = 0

    while idx < len(matrix):
        Tl += matrix[idx][idx]
        Tr += matrix[idx][(matrix_len - 1) - idx]

        idx += 1 
    
    return Tl + Tr

