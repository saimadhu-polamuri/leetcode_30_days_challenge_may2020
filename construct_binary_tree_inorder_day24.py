__author__ = "saimadhu.polamuri"

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:

        in_order = sorted(preorder)
        return self.bst_from_preorder_and_inorder(preorder, in_order)

    def bst_from_preorder_and_inorder(self, preorder, in_order):

        lenght_pre = len(preorder)
        lenght_in = len(in_order)

        if lenght_pre != lenght_in or preorder == None or in_order == None or lenght_pre == 0:
            return None

        root = TreeNode(preorder[0])
        root_index = in_order.index(root.val)

        root.left = self.bst_from_preorder_and_inorder(preorder[1:root_index + 1], in_order[: root_index])
        root.right = self.bst_from_preorder_and_inorder(preorder[root_index + 1:], in_order[root_index+ 1: ])
        return root






















