__author__ = "saimadhu.polamuri"

class Solution:
    def isPerfectSquare(self, num: int) -> bool:

        if num < 2:
            return True
        start = 2
        end = num
        while start <= end :
            mid = (start + end) // 2
            mid_square = mid * mid

            if mid_square == num:
                return True
            if mid_square > num:
                end = mid - 1
            if mid_square < num:
                start = mid + 1
        return False

test_solution = Solution()
print(test_solution.isPerfectSquare(16))
