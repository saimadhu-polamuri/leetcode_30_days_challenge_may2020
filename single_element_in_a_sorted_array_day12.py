__author__ = "saimadhu.polamuri"


class Solution:
    def singleNonDuplicate(self, nums):

        array_len = len(nums)
        i = 0
        if array_len == 1:
            return nums[i]
        while i < array_len - 1:
            if nums[i] != nums[i + 1]:
                return nums[i]
            i += 2
        return nums[i]


test_solution = Solution()
# nums = [3,3,7,7,10,11,11]
nums = [1,1,2]
print(test_solution.singleNonDuplicate(nums))
