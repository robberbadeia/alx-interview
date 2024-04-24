#!/usr/bin/python3
"""
0. Pascal's Triangle
"""


def pascal_triangle(n):
    """Generate Pascal's triangle up to n rows."""
    triangle = []  # This will contain the full triangle
    if n > 0:
        for i in range(n):
            row = [1] * (i + 1)  # Start each row with 1s
            for j in range(1, i):
                row[j] = triangle[i-1][j-1] + \
                    triangle[i-1][j]  # Calculate the inner values of the row
            triangle.append(row)  # Append the completed row to the triangle
    return triangle
