# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        output = []
        stack = []
        current = root

        while current or stack:
           
            while current:
                stack.append(current)
                current = current.left
            
            # 2. No more Left! Pop the last house we saved
            current = stack.pop()
            
            # 3. Record the value
            output.append(current.val)
            
            # 4. Now, try to go Right once
            current = current.right
            
        return output
        
        
        return output
