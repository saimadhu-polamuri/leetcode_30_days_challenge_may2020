__author__ = "saimadhu.polamuri"




# def test_print(a):
#
#     a_len = len(a)
#     mid = a_len // 2
#     for i in range(0, mid):
#         print(a[i])
#         print(a[(a_len - i) - 1])
#     if a_len % 2 != 0:
#         print (a[mid])

class Solution:
    def findJudge(self, N, trust):

        trust_count = len(trust)
        if trust_count < N-1:
            return -1
        if N == 1:
            return N
        trust_info = [0] * N
        mid = trust_count // 2
        for i in range(0, mid):

            # Traversing left to right
            in_index = trust[i][1]
            out_index = trust[i][0]
            trust_info[in_index - 1] += 1
            trust_info[out_index - 1] -= 1

            # Traversing right to left
            in_index = trust[(trust_count - i) - 1][1]
            out_index = trust[(trust_count - i) - 1][0]
            trust_info[in_index - 1] += 1
            trust_info[out_index - 1] -= 1
        if trust_count % 2 != 0:
            # Handel the mid case
            in_index = trust[mid][1]
            out_index = trust[mid][0]
            trust_info[in_index - 1] += 1
            trust_info[out_index - 1] -= 1

        # Use trust info to get the town judge
        mid = N // 2
        if N % 2 != 0:
            if trust_info[mid] == N - 1:
                return mid + 1
        for i in range(0, mid):

            if trust_info[i] == N - 1:
                return i + 1
            if trust_info[(N - i) - 1] == N - 1:
                return N - i
        return -1


test_solution = Solution()
# n = 2
# trust = [[1, 2]]
N = 7
trust = [[7,3],[1,3],[5,6],[2,1],[1,6],[3,7],[7,2],[1,2],[7,6],[6,3],[3,6],[5,7],[5,3],[6,4],[5,4],[2,6],[7,1],[1,4],[2,3],[6,5],[3,5],[3,4],[3,1],[7,4],[5,2],[2,4]]
print(test_solution.findJudge(N, trust))
# a = [1,2]
# test_print(a)
