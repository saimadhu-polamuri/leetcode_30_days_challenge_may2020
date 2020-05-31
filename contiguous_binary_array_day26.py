__author__ = "saimadhu.polamuri"

class Solution:
    def findMaxLength(self, nums):

        num_len = len(nums)
        counter = 0
        max_length = 0
        counters_dict = {}
        i = 0
        if num_len == 0:
            return 0

        while i < num_len:

            if nums[i] == 1:
                counter += 1
            if nums[i] == 0:
                counter -= 1
            if counter == 0:
                max_length = max(max_length, i + 1)
            if counter in counters_dict:
                max_length = max(max_length, i - counters_dict[counter])
            else:
                counters_dict[counter] = i
            i += 1
        return max_length


test_solution = Solution()
# A = [0, 1, 1, 0, 1, 1]
# A = [0]
A = [0,0,1,0,0,0,1,1]
print(test_solution.findMaxLength(A))
