__author__ = "saimadhu.polamuri"


class Solution:
    def checkStraightLine(self, coordinates):

        is_straight_line = True
        coordinates_len = len(coordinates)

        if coordinates_len > 2:
            x0, y0 = coordinates[0]
            x1, y1 = coordinates[1]
            y_delta = y1 - y0
            x_delta = x1 - x0
            for i in range(2, coordinates_len):
                x, y = coordinates[i]
                if y_delta * (x - x0) != x_delta * (y - y0):
                    is_straight_line = False
                    break
        return is_straight_line


test_solution = Solution()
# a = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
a = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
# a = [[-3,-2],[-1,-2],[2,-2],[-2,-2],[0,-2]]
# a = [[0,1],[1,3],[-4,-7],[5,11]]
print (test_solution.checkStraightLine(a))