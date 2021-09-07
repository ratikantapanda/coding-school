class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def branch_sum(root):
    sums = []
    calculate_sum(root, 0, sums)
    return sums

def calculate_sum(node, running_sum, sums):
    new_running_sum = running_sum + node.value
    if node.left is None or node.right is None:
        sums.append(new_running_sum)
        return
    calculate_sum(node.left, new_running_sum, sums)
    calculate_sum(node.right, new_running_sum, sums)