class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        for y in range(len(matrix) // 2):
            for x in range(len(matrix[y]) // 2):
                nx = len(matrix[y]) - y
                ny = len(matrix) - x