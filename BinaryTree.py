class Node(object):

    def __init__(self, data=None, *args, **kwargs):
        self._data = data
        self._left = None
        self._right = None
        self._parent = None

    def setData(self, data):
        self._data = data

    def setLeft(self, left):
        self._left = left
        left._parent = self

    def setRight(self, right):
        self._right = right
        right._parent = self

    def getData(self):
        return self._data

    def getLeft(self):
        return self._left

    def getRight(self):
        return self._right

    def setParent(self, parent):
        self._parent = parent

    def getParent(self):
        return self._parent


class BinaryTree(object):

    def __init__(self, root=None, *args, **kwargs):
        self._root = root

    def isEmpty(self):
        return (self._root is None)

    def setRoot(self, node):
        self._root = node

    def getRoot(self):
        return self._root

    def bfsTraversal(self):
        from collections import deque
        d = deque()
        d.append(self._root)
        while len(d):
            n = d.popleft()
            print n.getData(),
            if n.getLeft():
                d.append(n.getLeft())
            if n.getRight():
                d.append(n.getRight())

    @staticmethod
    def inorder(node):
        if node:
            BinaryTree.inorder(node.getLeft())
            print node.getData(),
            BinaryTree.inorder(node.getRight())

    @staticmethod
    def preorder(node):
        if node:
            print node.getData(),
            BinaryTree.preorder(node.getLeft())
            BinaryTree.preorder(node.getRight())

    @staticmethod
    def postorder(node):
        if node:
            BinaryTree.postorder(node.getLeft())
            BinaryTree.postorder(node.getRight())
            print node.getData(),

    def dfsTraversal(self):
        stack = []
        stack.append(self._root)
        while len(stack):
            n = stack.pop()
            print n.getData(),
            if n.getLeft():
                stack.append(n.getLeft())
            if n.getRight():
                stack.append(n.getRight())

    def printTree(self, traversal='bfs'):
        if traversal == 'dfs':
            self.dfsTraversal()
        elif traversal == 'bfs':
            self.bfsTraversal()
        else:
            raise Exception("traversal can be only dfs or bfs")

    def count(self):
        c = 0
        stack = []
        stack.append(self._root)
        while len(stack):
            n = stack.pop()
            c += 1
            if n.getLeft():
                stack.append(n.getLeft())
            if n.getRight():
                stack.append(n.getRight())
        return c

    @classmethod
    def createTree(cls, node_num=0):
        from collections import deque
        queue = deque()
        bt = BinaryTree()
        nodes = deque()

        for i in range(node_num):
            nodes.append(Node(i))

        while nodes:
            if bt.isEmpty():
                n = nodes.popleft()
                bt.setRoot(n)
                queue.append(n)
            else:
                n = queue.popleft()
                if nodes:
                    l = nodes.popleft()
                    n.setLeft(l)
                    queue.append(l)

                if nodes:
                    r = nodes.popleft()
                    n.setRight(r)
                    queue.append(r)

        bt.printTree()
        return bt


if __name__ == '__main__':
    print "Tree"
    l = BinaryTree.createTree(10)
    print "\ninorder"
    BinaryTree.inorder(l.getRoot())
    print "\npreorder"
    BinaryTree.preorder(l.getRoot())
    print "\npostorder"
    BinaryTree.postorder(l.getRoot())

    print "\nTotal nodes", l.count()
    assert l.count() == 10
