class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        wh = len(matrix) - 1
        for y in range(len(matrix) // 2):
            for x in range((len(matrix) + 1) // 2):
                old_lt_x, old_lt_y = x, y
                new_lt_x, new_lt_y = y, wh - x

                old_rt_x, old_rt_y = wh - y, x
                new_rt_x, new_rt_y = x, y

                old_rb_x, old_rb_y = wh - x, wh - y
                new_rb_x, new_rb_y = wh - y, x

                old_lb_x, old_lb_y = y , wh - x
                new_lb_x, new_lb_y = wh - x, wh - y

                matrix[old_lt_y][old_lt_x], matrix[old_rt_y][old_rt_x], \
                matrix[old_rb_y][old_rb_x], matrix[old_lb_y][old_lb_x] \
                = matrix[new_lt_y][new_lt_x], matrix[new_rt_y][new_rt_x], \
                matrix[new_rb_y][new_rb_x], matrix[new_lb_y][new_lb_x]


if __name__ == "__main__":
    obj = Solution()
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    obj.rotate(matrix)