__author__ = "saimadhu.polamuri"

# For search info we need both the depth and the parent info.

class SearchKey:

    def __init__(self, value):

        self.value = value
        self.depth = None
        self.parent = None


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:

        # initialization of the keys to search
        # key_1 = SearchKey(x)
        # key_2 = SearchKey(y)
        x_info = list()
        y_info = list()
        depth = 0
        parent = None
        if root is None:
            return False

        self.search_binary_tree(root, x, y, depth, parent, x_info, y_info)

        # Value will be true when key1 and key2 depth is same and
        # parents are different
        return x_info[0][0] == y_info[0][0] and x_info[0][1] != y_info[0][1]

    def search_binary_tree(self, root, key_1, key_2, depth, parent, x_info, y_info):

        if root is None:
            return None
        if root is
        if root.val == key_1:
            x_info.append((depth, parent))

        if root.val == key_2:
            y_info.append((depth, parent))

        self.search_binary_tree(root.left, key_1, key_2, depth+1, parent, x_info, y_info)
        self.search_binary_tree(root.right, key_1, key_2, depth + 1, parent, x_info, y_info)





