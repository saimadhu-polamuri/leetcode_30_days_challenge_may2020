__author__ = "saimadhu.polamuri"

import math

class Solution:
    # Approach 01
    def majorityElement(self, nums) -> int:

        array_len = len(nums)
        if array_len > 0:
            majority_element = nums[0]
            majority_element_frequency = 1

            if array_len > 1:
                hash_map = dict()
                threshhold_num = math.floor(array_len / 2)

                for i in range(0, array_len):
                    if nums[i] in hash_map.keys():
                        hash_map[nums[i]] += 1
                        if hash_map[nums[i]] > majority_element_frequency:
                            majority_element = nums[i]
                            majority_element_frequency = hash_map[nums[i]]
                    else:
                        hash_map[nums[i]] = 1
        return majority_element

    # Approach 02
    def majorityElement(self, nums) -> int:
        nums.sort()
        length = len(nums) // 2
        return nums[length]


test_solution = Solution()

# a = [3,2,3]
# a = [2,2,1,1,1,2,2]
# a = [1]
# a = [6,6,6,7,7]
a = [6,6,6,7,7,7]
print(test_solution.majorityElement(a))