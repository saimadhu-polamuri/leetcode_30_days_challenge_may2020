__author__ = "saimadhu.polamuri"

class Solution:
    def maxUncrossedLines(self, A, B ):

        a_len = len(A)
        b_len = len(B)

        matrix = [[0 for i in range(b_len + 1)] for j in range(a_len + 1)]

        for i in range(a_len):
            for j in range(b_len):
                if A[i] == B[j]:
                    matrix[i + 1][j + 1] = matrix[i][j] + 1
                else:
                    matrix[i + 1][j + 1] = max(matrix[i + 1][j], matrix[i][j + 1])
        return matrix[a_len][b_len]


test_solution = Solution()
# A = [1,4,2]
# B = [1,2,4]

# A = [2,5,1,2,5]
# B = [10,5,2,1,5,2]

# A = [1,3,7,1,7,5]
# B = [1,9,2,5,1]

A = [4,6]
B = [1,9,2,5,1]
print(test_solution.maxUncrossedLines(A, B))
