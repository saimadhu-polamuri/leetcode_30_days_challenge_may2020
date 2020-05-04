__author__ = "saimadhu.polamuri"

class Solution:

    def get_stone_wise_count(self, s):

        stones_count = {}

        for i in range(0, len(s)):

            key = s[i]

            if key in stones_count.keys():
                stones_count[key] +=1
            else:
                stones_count[key] = 1

        return stones_count

    def get_stone_count(self, j, s):

        stone_wise_count = self.get_stone_wise_count(s)

        stones = stone_wise_count.keys()

        stone_count = 0
        for i in range(0, len(j)):
            key = j[i]
            if key in stones:
                stone_count += stone_wise_count[key]

        return stone_count

    def numJewelsInStones(self, J: str, S: str) -> int:

        return self.get_stone_count(j, s)



