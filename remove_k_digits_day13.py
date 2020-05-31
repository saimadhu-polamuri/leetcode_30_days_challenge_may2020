__author__ = "saimadhu.polamuri"

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:

        stack = []
        number_to_remove = k
        for current_element in num:
            while number_to_remove and stack and stack[-1] > current_element:
                stack.pop()
                number_to_remove = number_to_remove -1
            stack.append(current_element)

        answer = "".join(stack[0: len(num)-k]).lstrip("0")
        # print ("Answer ::{}".format(answer))
        if len(answer):
            return answer
        else:
            return "0"

test_solution = Solution()
num = "112"
k = 1
# num = "1432219"
# k = 3
print(test_solution.removeKdigits(num, k))