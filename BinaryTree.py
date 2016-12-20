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
        from random import randint
        bt = BinaryTree()
        nodes = []
        stack = []

        for i in range(node_num):
            # d = randint(0, node_num)
            nodes.append(Node(i))

        while len(nodes):
            if bt.isEmpty():
                n = nodes.pop()
                bt.setRoot(n)
                stack.append(n)
            else:
                n = stack.pop()
                if len(nodes):
                    r = nodes.pop()
                    n.setRight(r)
                    stack.append(r)
                if len(nodes):
                    l = nodes.pop()
                    n.setLeft(l)
                    stack.append(l)

        bt.printTree()
        return bt


if __name__ == '__main__':
    l = BinaryTree.createTree(10)
    print l.count()
    assert l.count() == 10
