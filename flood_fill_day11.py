__author__ = "saimadhu.polamuri"

class Solution:
    def floodFill(self, image, sr, sc, newColor):

        self.color = image[sr][sc]
        self.newColor = newColor
        self.image = image
        self.total_rows = len(self.image)
        self.total_columns = len(self.image[0])
        if self.color == self.newColor:
            return self.image
        self.flood_fill_helper(sr, sc)
        return self.image

    def flood_fill_helper(self, sr, sc):
        if self.image[sr][sc] == self.color:
            self.image[sr][sc] = self.newColor

            if sr >= 1:
                self.flood_fill_helper(sr-1, sc)
            if sr+1 < self.total_rows:
                self.flood_fill_helper(sr+1, sc)
            if sc >= 1:
                self.flood_fill_helper(sr, sc-1)
            if sc+1 < self.total_columns:
                self.flood_fill_helper(sr, sc+1)

test_solution = Solution()
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
newColor = 2
print(test_solution.floodFill(image,sr,sc,newColor))



