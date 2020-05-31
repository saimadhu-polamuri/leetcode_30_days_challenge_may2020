__author__ = "saimadhu.polamuri"

import math

class Solution:
    def kClosest(self, points, K):
    	total_points = len(points)
		distance_dict = {}
    	for i in range(total_points):
    		distance_dict[i] = self.get_distance_with_origin(points[i])
    	# sort the dictionary keys by values
    	keys = sorted(distance_dict, key = lambda x: distance_dict[x])
    	result_points = []
    	for i in range(k):
    		result_points.append(points[keys[i]])
    	return result_points


    def get_distance_with_origin(self, point):
    	distance = math.sqrt(pow(point[0], 2) + pow(point[1], 2))
    	return distance


test_solution = Solution()

# points = [[3,3],[5,-1],[-2,4]]
# k = 1
points = [[1,3],[-2,2]]
k = 1
print(test_solution.kClosest(points, k))