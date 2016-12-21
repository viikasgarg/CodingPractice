class Node(object):

    def __init__(self, data=None, *args, **kwargs):
        self.data = data
        self._children = {}
        self._end = False

    def setEnd(self):
        self._end = True

    def getEnd(self):
        return self._end

    def setChild(self, value):
        if not self._children.get(value):
            self._children[value] = Node()
        return self._children.get(value)

    def getChild(self, value):
        return self._children.get(value)


class Trie(object):

    def __init__(self, *args, **kwargs):
        self._root = Node()

    def insertKey(self, key):
        temp = self._root
        for k in key:
            temp = temp.setChild(k)
        temp.setEnd()

    def findKey(self, key):
        temp = self._root
        for k in key:
            temp = temp.getChild(k)
            if not temp:
                return False
        return temp.getEnd()

    def printTrie(self, node):
        pass

if __name__ == '__main__':
    t = Trie()
    keys = ['vikas', "vika", "garg"]
    for k in keys:
        t.insertKey(k)
    assert t.findKey("vikas")
    assert not t.findKey("vi")
    assert t.findKey("vika")
    assert not t.findKey("ASSASA")
