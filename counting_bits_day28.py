__author__ = "saimadhu.polamuri"

class Solution:
    def countBits(self, num):

        bit_counts = []
        bit_counts.append(0)

        for i in range(1, num + 1):

            bit_counts.append(bit_counts[i//2] + int(i&1))
        return bit_counts


test_solution = Solution()
a = 2
print(test_solution.countBits(a))
