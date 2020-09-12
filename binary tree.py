class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
def Longst_road(current,parent,longest_end_at_parent):
    if not current:
        return longest_end_at_parent
    size=1
    if parent and current.val==parent.val+1:
        size=longest_end_at_parent+1
    return max(longest_end_at_parent, Longst_road(current.left,current,size) ,Longst_road(current.right,current,size))

root=TreeNode(1)
root.left=TreeNode(None)
root.right=TreeNode(3)
root.right.left=TreeNode(2)
root.right.right=TreeNode(4)
root.right.right.left=TreeNode(None)
root.right.right.right=TreeNode(5)
root.right.right.right.left=TreeNode(8)
root.right.right.right.right=TreeNode(9)
find_the_longest=Longst_road(root,None,0)
print(find_the_longest)