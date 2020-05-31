__author__ = "saimadhu.polamuri"


class Solution:
    def intervalIntersection(self, A, B):

        a_len = len(A)
        b_len = len(B)

        if a_len == 0 or b_len == 0:
            return []

        result_intervals = list()

        i = 0
        j = 0
        while (i < a_len) and (j < b_len):
            max_first = max(A[i][0], B[j][0])
            min_second = min(A[i][1], B[j][1])

            if max_first <= min_second:
                result_intervals.append([max_first, min_second])

            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1

        return result_intervals


test_solution = Solution()

A = [[0,2],[5,10],[13,23],[24,25]]
B = [[1,5],[8,12],[15,24],[25,26]]

print (test_solution.intervalIntersection(A, B))