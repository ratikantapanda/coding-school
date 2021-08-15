class Node:
    def __init__(self,data=None,left=None,right=None):
        self.data = data
        self.left =left
        self.right = right

def inorder_r(root):
    result = []
    _inorder_r(root,result)
    return result

def _inorder_r(root,result):
    if root is None:
        return
    _inorder_r(root.left,result)
    #print(root.data, end=' ')
    result.append(root.data)
    _inorder_r(root.right,result)


def inorder(root):
    result = []
    stack = []
    while root != None or len(stack) != 0:
        if root != None:
            stack.append(root)
            root = root.left
        else:
            root = stack.pop()
            result.append(root.data)
            root = root.right
    return result



if __name__ == '__main__':
    """ Construct the following tree
               1
             /   \
            /     \
           2       3
          /      /   \
         /      /     \
        4      5       6
              / \
             /   \
            7     8
    """

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.right.left.left = Node(7)
    root.right.left.right = Node(8)
    result= inorder_r(root)
    print(result)
    print()
    result = inorder(root)
    print(result)
