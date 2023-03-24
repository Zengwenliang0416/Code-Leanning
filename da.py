def submatrix_sums(matrix, queries):
    """
    计算给定矩阵中指定多个子矩阵的元素和。

    :param matrix: 二维列表，表示输入矩阵
    :param queries: 列表，其中每个元素都是一个元组，表示一个子矩阵的左上角和右下角坐标
    :return: 列表，其中每个元素都是一个整数，表示对应子矩阵中元素的和
    """
    rows, cols = len(matrix), len(matrix[0])

    # 计算二维前缀和矩阵 prefix_sum
    prefix_sum = [[0] * (cols + 1) for _ in range(rows + 1)]
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            prefix_sum[i][j] = prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j - 1] + matrix[i - 1][j - 1]

    # 计算所有子矩阵的元素和
    submatrix_sums = [[0] * cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows):
                for l in range(j, cols):
                    submatrix_sums[i][j] += prefix_sum[k + 1][l + 1] - prefix_sum[k + 1][j] - prefix_sum[i][l + 1] + prefix_sum[i][j]

    # 计算每个子矩阵的元素和
    results = []
    for query in queries:
        top_left, bottom_right = query
        row1, col1 = top_left
        row2, col2 = bottom_right
        results.append(submatrix_sums[row1][col1] - submatrix_sums[row1][col2 + 1] - submatrix_sums[row2 + 1][col1] + submatrix_sums[row2 + 1][col2 + 1])

    return results


def submatrix_sums(matrix, queries):
    rows, cols = len(matrix), len(matrix[0])

    # 计算每个 (i, j) 到矩阵左上角的元素和
    prefix_sums = [[0] * (cols + 1) for _ in range(rows + 1)]
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            prefix_sums[i][j] = (
                    matrix[i - 1][j - 1] + prefix_sums[i - 1][j]
                    + prefix_sums[i][j - 1] - prefix_sums[i - 1][j - 1])

    # 计算每个子矩阵的元素和
    submatrix_sums = []
    for query in queries:
        (top, left), (bottom, right) = query
        submatrix_sum = (
                prefix_sums[bottom + 1][right + 1] - prefix_sums[bottom + 1][left]
                - prefix_sums[top][right + 1] + prefix_sums[top][left])
        submatrix_sums.append(submatrix_sum)

    return submatrix_sums
import os
import sys

# 请在此输入您的代码
def sqrt(x):
    return int(x**0.5)

def is_sqrt(x):
    return sqrt(x)*sqrt(x)==x
def supper(n,k):
    return sqrt(n/k)

N=int(input())
for a in range(supper(N,4)):
    i = a*a
    for b in range(a,supper(N,3)):
        j = i + b*b
        for c in range(b,supper(N,2)):
            k = c*c + j
            d_square = N-k
            if d_square >= c*c:
                if is_sqrt(d_square):
                    d = sqrt(d_square)
                    print(a,' ')
                    print(b,' ')
                    print(c,' ')
                    print(d)