# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def inorderTraversal(root):
    result, stack = [], [(root, False)]

    while stack:
        cur, visited = stack.pop()
        if cur:
            if visited:
                result.append(cur.val)
            else:
                stack.append((cur.right, False))
                stack.append((cur, True))
                stack.append((cur.left, False))
    return result