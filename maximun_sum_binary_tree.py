class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def inorderTraverse(root):
    output=[]
    stack=[(root,1)]
    while stack:
        node,count=stack.pop()
        if count==1:
            stack.append((node,count+1))
            if node.left:
                stack.append((node.left,1))
        if count==2:
            output.append(node.val)
            if node.right:
                stack.append((node.right, 1))
    return output

class maximun_sum(object):
    def maximum_sub(self,root):
        if not root:
            return 0
        self.retVal=float('-inf')
        self.helper(root)
        return self.retVal

    def helper(self,root):
        if not root:
            return 0
        if root.left is None and root.right is None:
            return root.val
        self.helper(root.left)
        self.helper(root.right)
        if root.left and root.right:
            self.retVal=max(self.retVal,root.left.val+root.right.val+root.val)
            return max(root.left.val,root.right.val)+root.val
        else:
            return root.right.val+root.val if root.left is None else root.left.val+root.val


root1=TreeNode(10)
root1.left=TreeNode(5)
root1.right=TreeNode(15)
root1.left.left=TreeNode(2)
root1.left.right=TreeNode(7)
root1.right.left=TreeNode(12)
root1.right.right=TreeNode(20)

w=inorderTraverse(root1)
print(w)

sum= maximun_sum()
print(sum.maximum_sub(root1))