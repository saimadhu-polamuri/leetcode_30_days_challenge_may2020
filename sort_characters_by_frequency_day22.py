__author__ = "saimadhu.polamuri"

class Solution:
    def frequencySort(self, s):

        # Frequency dict
        frequency_dict = {}

        for element in s:
            if element in frequency_dict:
                frequency_dict[element] += 1
            else:
                frequency_dict[element] = 1

        # Sorting the dict
        sorted_list = sorted(frequency_dict, key= lambda x: frequency_dict[x], reverse=True)
        result_string = ''
        for key in sorted_list:
            result_string += key * frequency_dict[key]

        return result_string


test_solution = Solution()
s = "tree"
print(test_solution.frequencySort(s))