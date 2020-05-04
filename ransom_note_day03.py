__author__ = "saimadhu.polamuri"

"""Given an arbitrary ransom note string and another string containing letters from all the magazines, 
write a function that will return true if the ransom note can be constructed from the magazines ; 
otherwise, it will return false."""

import pdb

class Solution:


    def get_hash_map(self, string):

        string_len = len(string)
        hash_map = dict()

        for i in range(0, string_len):

            key = string[i]
            if key in hash_map.keys():
                hash_map[key] += 1
            else:
                hash_map[key]  = 1
        return hash_map



    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        can_construct = False
        magazine_len = len(magazine)
        ransom_len = len(ransomNote)


        if ransom_len == 0:
            can_construct = True

        else:
            ranson_hash = self.get_hash_map(ransomNote)
            magazine_hash = self.get_hash_map(magazine)
            count = 0
            for key in ranson_hash.keys():

                if key in magazine_hash.keys():
                    if ranson_hash[key] <= magazine_hash[key]:
                        count += 1
            if count == len(ranson_hash.keys()):
                can_construct = True

        return can_construct



test_solution = Solution()

ransom_notes = ["a", "aa", "aa", "", "bg", "fffbfg"]
magazines = ["b", "ab", "aab", "", "efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj", "effjfggbffjdgbjjhhdegh"]

print(test_solution.canConstruct(ransom_notes[1], magazines[1]))



