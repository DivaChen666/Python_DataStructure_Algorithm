class TreeNode(object):
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None

class binary_search_Tree(object):
    def __init__(self):
        self.root=None
    def _query(self,root,key):
        if not root:
            return None
        if key==root.key:
            return root.value
        elif key>root.key:
            return self._query(root.right,key)
        else:
            return self._query(root.left, key)
    def query(self,root,key):
        return self._query(root,key)

    def _Min(self,root):
        if not root.left:
            return root
        return self._Min(root.left)

    def _deletMin(self,root):
        if not root.left:
            return root.right
        root.left=self._deletMin(root.left)
        return root

    def _delet(self,root,key):
        if not root:
            return None
        if key<root.key:
            root.left=self._delet(root.left, key)
        elif key>root.key:
            root.right=self._delet(root.right, key)
        else:
            if not root.right:
                return root.left
            if not root.left:
                return root.right
            t=root
            root=self._Min(t.right)
            root.right=self._deletMin(t.right)
            root.left=t.left
        return root

    def delete(self,key):
        self.root=self._delet(self.root,key)


def preorder(root):
    output=[]
    if root is None:
        return output
    stack=[(root,1)]
    while stack:
        node,count=stack.pop()
        if count==1:
            output.append(node.key)
            stack.append((node,count+1))
            if node.left:
                stack.append((node.left,1))
        if count==2:
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


gagaga=preorder(root1)
print(gagaga)

a=binary_search_Tree()
a.root = root1

a.delete(5)

gagaga=preorder(a.root)
print(gagaga)












