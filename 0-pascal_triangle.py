#!/user/bin/python3
"""Pascal'S Triangle"""


def pascal_triangle(n):
    """Return a list representing a Pascal's triangle of number n"""
    if n <= 0:
        return []

    pascal_triangle = [[1]]
    for i in range(1, n):
        list = [1]
        for j in range(1, i):
            list.append(pascal_triangle[-1][j - 1] + pascal_triangle[-1][j])
        list.append(1)
        pascal_triangle.append(list)
    return pascal_triangle
