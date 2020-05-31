__author__ = "saimadhu.polamuri"

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        s1_len = len(s1)
        s2_len = len(s2)

        if s2_len < s1_len:
            return False
        s1_dict = self.get_frequency_dict(s1)
        start = 0
        end = start + s1_len
        s2_dict = self.get_frequency_dict(s2[start:end])
        if s1_dict == s2_dict:
            return True

        for i in range(1, s2_len - s1_len + 1):

            # remove the left side element and adding the right side element
            # remove the left side element the s2_dict
            start = i - 1
            end = start + s1_len

            if s2_dict[s2[start]] > 1:
                s2_dict[s2[start]] -= 1
            else:
                del s2_dict[s2[start]]
            # Add the right side elements into the dict
            if s2[end] in s2_dict.keys():
                s2_dict[s2[end]] += 1
            else:
                s2_dict[s2[end]] = 1
            if s1_dict == s2_dict:
                return  True
        return False

    def get_frequency_dict(self, string):

        frequency_dict = dict()

        for key in string:
            if key in frequency_dict.keys():
                frequency_dict[key] += 1
            else:
                frequency_dict[key] = 1
        return frequency_dict

test_solution = Solution()
s1 = "b"
s2 = "oaoo"
print(test_solution.checkInclusion(s1, s2))