#!/bin/python3

import math
import os
import random
import re
import sys

input = sys.stdin.readline


#
# Complete the 'getBingoNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY mat
#  2. INTEGER_ARRAY arr
#


def getBingoNumber(mat, arr):
    # Write your code here
    position_hash = {}
    for y in range(len(mat)):
        for x in range(len(mat[y])):
            position_hash[mat[y][x]] = [x, y]

    x_axis_bingo_count = [0 for _ in range(mat_rows)]
    y_axis_bingo_count = [0 for _ in range(mat_columns)]

    for i in arr:
        x_axis_bingo_count[position_hash[i][1]] += 1
        y_axis_bingo_count[position_hash[i][0]] += 1

        if x_axis_bingo_count[position_hash[i][1]] == mat_columns:
            return i
        if y_axis_bingo_count[position_hash[i][0]] == mat_rows:
            return i


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    mat_rows = int(input().strip())
    mat_columns = int(input().strip())

    mat = []

    for _ in range(mat_rows):
        mat.append(list(map(int, input().rstrip().split())))

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = getBingoNumber(mat, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
