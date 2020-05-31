__author__ = "Saimadhu.Polamuri"

class Solution:
	def minDistance(self, word1: str, word2: str) -> int:

		word1_len = len(word1)
		word2_len = len(word2)


		distance_matrix = [[0 for i in range(word2_len + 1)] for j in range(word1_len + 1)]
		for i in range(word1_len + 1):
			for j in range(word2_len + 1):
				if i == 0:
					distance_matrix[0][j] = j
				elif j == 0:
					distance_matrix[i][0] = i
				elif word1[i - 1] == word2[j - 1]:
					distance_matrix[i][j] = distance_matrix[i - 1][j - 1]
				else:
					distance_matrix[i][j] = 1 + min(distance_matrix[i - 1][j], distance_matrix[i][j - 1], 
						distance_matrix[i - 1][j - 1])

		return distance_matrix[word1_len][word2_len]
