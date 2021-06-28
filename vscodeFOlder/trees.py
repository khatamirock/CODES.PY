class node:
    def __init__(self, val):
        self.dat = val
        self.left = None
        self.right = None


def preOrdr(root):
    if root is not None:
        print(root.dat)
        preOrdr(root.left)
        preOrdr(root.right)


def insert(root, node):
    if root is None:
        root = node
        return
    if root.dat < node.dat:
        if root.right is None:
            root.right = node
        else:
            insert(root.right, node)
    else:
        if root.left is None:
            root.left = node
        else:
            insert(root.left, node)


root = node(7)


insert(root, node(9))
insert(root, node(8))
insert(root, node(1))
insert(root, node(4))
insert(root, node(5))
insert(root, node(4))
insert(root, node(6))
insert(root, node(3))
insert(root, node(2))

preOrdr(root)
