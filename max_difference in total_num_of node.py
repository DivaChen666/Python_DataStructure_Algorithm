class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def preorder(root):
    output=[]
    if root is None:
        return output
    stack=[(root,1)]
    while stack:
        node,count=stack.pop()
        if count==1:
            output.append(node.val)
            stack.append((node,count+1))
            if node.left:
                stack.append((node.left,1))
        if count==2:
            if node.right:
                stack.append((node.right,1))
    return output


global_max=-1
res=None
def find_the_bigges_node(root):
    global global_max
    global res
    biggest_node(root)
    return res

def biggest_node(root):

    if root is None:
        return 0
    # if root.left is None and root.right is None:
    #     return 1
    left_total=biggest_node(root.left)
    right_total=biggest_node(root.right)
    global global_max
    global res
    if abs(left_total-right_total)>global_max:
        global_max=abs(left_total-right_total)
        res=root
    return left_total+right_total+1

root=TreeNode(1)
root.left=TreeNode('null')
root.right=TreeNode(3)
root.right.left=TreeNode(2)
root.right.right=TreeNode(4)
root.right.right.left=TreeNode('null')
root.right.right.right=TreeNode(5)
root.right.right.right.left=TreeNode(8)
root.right.right.right.right=TreeNode(9)


print(biggest_node(root))
print(res.val)
w=preorder(root)
print(w)