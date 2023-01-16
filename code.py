class Solution:
    def recoverTree(self, root: Optional[TreeNode]):
		# in-order travers this tree
        def inorder(node):
            if node:
                return inorder(node.left) + [node] + inorder(node.right)
            return []
        
		# get the in-order list of nodes
        temp = inorder(root)
		# sort all the values of the tree
        sort = [n.val for n in temp]
        sort.sort()
        
		# just copy all the value from sorted list
        for i in range(len(sort)):
            temp[i].val = sort[i]
	


