class Node:
    def __init__(self,data=None,left=None,right=None):
        self.data = data
        self.left =left
        self.right = right

# def inorder_r(root):
#     result = []
#     _inorder_r(root,result)
#     return result
#
# def _inorder_r(root,result):
#     if root is None:
#         return
#     _inorder_r(root.left,result)
#     #print(root.data, end=' ')
#     result.append(root.data)
#     _inorder_r(root.right,result)

def inorder_r(root):
    result = []
    def inorder(root):
        if root is None:
            return
        inorder(root.left)
        # print(root.data, end=' ')
        result.append(root.data)
        inorder(root.right)
    inorder(root)
    return result

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


def preorder_r(root):
    result=[]
    def preorder(root):
        if root is None:
            return
        result.append(root.data)
        preorder(root.left)
        preorder(root.right)
    preorder(root)
    return  result
def preorder(root):
    if root is None:
        return None
    result = []
    stack = []
    stack.append(root)
    while len(stack) !=0:
        temp = stack.pop()
        result.append(temp.data)
        if temp.right is not None:
            stack.append(temp.right)
        if temp.left is not None:
            stack.append(temp.left)
    return result

def postorder_r(root):
    result=[]
    def postorder(root):
        if root is None:
            return
        postorder(root.left)
        postorder(root.right)
        result.append(root.data)
    postorder(root)
    return  result

from collections import deque
def postorder(root):
    stack = []
    stack.append(root)
    result = deque()
    while stack:
        curr = stack.pop()
        result.appendleft(curr.data)
        if curr.left:
            stack.append(curr.left)
        if curr.right:
            stack.append(curr.right)
    return list(result)

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

    print("Inoder traverse")
    inorder_result= inorder_r(root)
    print(inorder_result)
    inorder_result = inorder(root)
    print(inorder_result)


    print("Preorder traverse")
    preorder_result = preorder_r(root)
    print(preorder_result)
    preorder_result = preorder(root)
    print(preorder_result)

    print("Postorder traverse")
    postorder_result = postorder_r(root)
    print(postorder_result)
    postorder_result = postorder(root)
    print(postorder_result)