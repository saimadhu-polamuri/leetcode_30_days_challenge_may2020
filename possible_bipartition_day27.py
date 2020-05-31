__author__ = "saimadhu.polamuri"


class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:

        dict = {}

        for pairs in dislikes:
            if pairs[0] in dict:
                dict[pairs[0]].add[pairs[1]]
            else:
                dict[pairs[0]] = set([pairs[1]])
            if pairs[1] in dict:
                dict[pairs[1]].add(pairs[0])
            else:
                dict[pairs[1]] = set([pairs[0]])

        seen = {}

        for i in range(1, N+1):
            if i not in seen:
                seen[i] = 0
                stack = [i]
                while stack:
                    a = stack.pop()
                    if a in dict:
                        for b in dict[a]:
                            if b in seen:
                                if seen[a] == seen[b]:
                                    return False
                            else:
                                seen[b] = (seen[a]+1) % 2
                                stack.append(b)
        return True
