class myNode(object):
    def __init__(self,v=0):
        ##previous --> left
        ##next --> right
        self.previous = None
        self.next = None
        self.val = v

class myTree(object):
    def __init__(self):
        self.root = myNode(250)

def inorder(root):
    if root:
        inorder(root.previous)
        print(root.val)
        inorder(root.next)

def insert_1(root,node):
    if (root is None):
        root = node
    else:
        if (root.val < node.val):
            if(root.next is None):
                root.next = node
            else:
                insert_1(root.next, node)
        else:
            if(root.previous is None):
                root.previous = node
            else:
                insert_1(root.previous, node)
def test():
    numbers = []
    for x in range(5):
        numbers.append(random.randint(1,101))
    numbers
    tree_1 = myTree()
    for n in numbers:
        insert_1(tree_1.root, myNode(n))
    inorder(tree_1.root)

test()


