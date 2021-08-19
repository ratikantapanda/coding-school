from collections import deque
class Node:
    def __init__(self,data=None,left=None,right=None):
        self.data = data
        self.left =left
        self.right = right


def level_order_print(root):
    if root is None:
        return None
    result = []
    stack = deque()
    stack.append(root)
    level=0
    while len(stack) != 0:
        length = len(stack)
        level = level + 1
        nodes=[]
        while length != 0:
            temp = stack.popleft()
            length = length -1
            nodes.append(temp.data)
            if temp.left is not None:
                stack.append(temp.left)
            if temp.right is not None:
                stack.append(temp.right)
        result.append((level,nodes))
    return result
def print_level_order(root):
    result= level_order_print(root)
    for x in result:
        level,data =x
        print("level-",level, "===>",data)
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
    result = level_order_print(root)
    print(result)
    print_level_order(root)