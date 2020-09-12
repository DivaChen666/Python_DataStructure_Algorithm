class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class getheight(object):
    def GetaBinaryTreeHeight(self,root):
        if root is None:
            return 0
        self.height=float('-inf')
        self.helper(root,0)
        return self.height


    def helper(self,root,depth):
        if root is None:
            self.height=max(self.height,depth)
            return
        depth+=1
        self.helper(root.left, depth)
        self.helper(root.right,depth)
        return

def preorder(root):
    output=[]
    if not root:
        return output
    stack=[(root,1)]
    while stack:
        node,counter=stack.pop()
        if counter==1:
            output.append(node.val)
            stack.append((node,counter+1))
            if node.left:
                stack.append((node.left,1))
        if counter==2:
            if node.right:
                stack.append((node.right,1))
    return output



root1=TreeNode(10)
root1.left=TreeNode(5)
root1.right=TreeNode(15)
root1.left.left=TreeNode(2)
root1.left.right=TreeNode(7)
root1.right.left=TreeNode(12)
root1.right.right=TreeNode(20)

w=preorder(root1)
print(w)
c= getheight()
print(c.GetaBinaryTreeHeight(root1))
