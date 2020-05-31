__author__ = "saimadhu.polamuri"

class Solution:
    def countSquares(self, matrix):

        n = len(matrix)
        m = len(matrix[0])

        ans_matrix = [[0] * (m + 1) for _ in range(n + 1)]
        count = 0

        for row in range(1, n+1):
            for col in range(1, m + 1):
                if matrix[row - 1][col - 1] == 1:
                    ans_matrix[row][col] = 1 + min(ans_matrix[row][col-1], ans_matrix[row-1][col],
                                                   ans_matrix[row - 1][col - 1])

                    count += ans_matrix[row][col]

        return count






















