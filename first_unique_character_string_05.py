__author__ = "saimadhu.polamuri"


class Solution:

    def firstUniqChar(self, s: str) -> int:

        result_index = -1
        hash_map = dict()
        hash_map_index = dict()
        string_len = len(s)
        unique_elements = list()
        for i in range(0, string_len):

            if s[i] in hash_map.keys():
                hash_map[s[i]] += 1
            else:
                hash_map[s[i]] = 1
                hash_map_index[s[i]] = i
                unique_elements.append(s[i])

        for element in unique_elements:

            if hash_map[element] == 1:
                result_index = hash_map_index[element]
                break

        return result_index



test_solution = Solution()
s = ["leetcode", "loveleetcode", "a", ""]
print(test_solution.firstUniqChar(s[3]))
