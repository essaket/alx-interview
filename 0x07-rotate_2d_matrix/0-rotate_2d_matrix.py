#!/usr/bin/python3
"""0. Rotate 2D Matrix"""


def rotate_2d_matrix(matrix):
    """Rotates a 2D matrix 90 degrees clockwise in place.

    Args:
    matrix (list of list of int): The matrix to rotate.

    Returns: None
    """
    # Get the size of the matrix (n x n)
    n = len(matrix)

    # Transpose the matrix by swapping elements across the diagonal
    for i in range(n):
        for j in range(i + 1, n):
            # Swap element at (i, j) with element at (j, i)
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row to achieve the 90-degree clockwise rotation
    for i in range(n):
        matrix[i].reverse()
