__author__ = "saimadhu.polamuri"


class Solution:
    def maxSubarraySumCircular(self, A):

        array_len = len(A)
        if array_len == 0:
            return 0
        if array_len == 1:
            return A[0]
        sub_array_max_sum = self.sub_array_max(A)
        sub_circle_array_max_sum = 0
        for i in range(array_len):
            sub_circle_array_max_sum += A[i]
            A[i] = - A[i]
        sub_circle_array_max_sum = sub_circle_array_max_sum + self.sub_array_max(A)

        if sub_circle_array_max_sum > sub_array_max_sum and sub_circle_array_max_sum != 0:
            return sub_circle_array_max_sum
        else:
            return sub_array_max_sum


    def sub_array_max(self, A):
        max_sum = A[0]
        total_sum = A[0]
        array_len = len(A)
        for i in range(1, array_len):
            total_sum = max(total_sum + A[i], A[i])
            max_sum = max(max_sum, total_sum)
        return max_sum

test_solution = Solution()
A = [-7,1,2,7,-2,-5]
# A = [5,-3,5]
# print(test_solution.maxSubarraySumCircular(A))
print(test_solution.maxSubarraySumCircular(A))