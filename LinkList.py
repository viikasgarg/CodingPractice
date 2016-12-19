class Node(object):
    def __init__(self, data=None, *args, **kwargs):
        self._data = data
        self._next = None

    def setData(self, data):
        self._data = data

    def setNext(self, next):
        self._next = next

    def getData(self):
        return self._data

    def getNext(self):
        return self._next


class LinkList(object):

    def __init__(self, head=None, *args, **kwargs):
        self.head = head

    def append_node(self, data):
        node = Node(data)

        if self.head:
            temp = self.head
            while temp.getNext():
                temp = temp.getNext()
            temp.setNext(node)
        else:
            self.head = node

    def insert_node(self, pos, data):
        node = Node(data)
        c = 0
        if pos == 0:
            node.setNext(self.head)
            self.head = node
        else:
            temp = self.head
            while c < pos:
                c += 1
                if temp:
                    temp = temp.getNext()
                else:
                    print "Item can't be inserted at position {} \
                        because list size is {}".format(pos, self.count())
                    return False
            node.setNext(temp.getNext())
            temp.setNext(node)
        return True

    def print_list(self):
        temp = self.head
        while temp:
            print temp.getData(),
            temp = temp.getNext()

    def count(self):
        temp = self.head
        c = 0
        while temp:
            temp = temp.getNext()
            c += 1
        return c

    @classmethod
    def create_list(cls, nodes=0):
        l = LinkList()
        p = LinkList()
        from random import randint
        for i in range(nodes):
            d = randint(0, nodes)
            l.append_node(d)
            p.insert_node(1, d)
        l.print_list()
        print "\n"
        p.print_list()
        return l

if __name__ == '__main__':
    l = LinkList.create_list(10)
    assert l.count() == 10
