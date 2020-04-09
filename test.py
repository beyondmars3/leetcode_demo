class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Tree:

    def __init__(self):
        self.head = None

    def add(self, val):
        _node = Node(val)
        if not self.head:
            self.head = _node
            return
        root = self.head
        q = [root]
        while q:
            c_node = q.pop(0)
            # 如果当前节点有下一个节点，则遍历直到最后，否则给下一个赋值
            if c_node.next is None:
                c_node.next = _node
                return
            q.append(c_node.next)

    def loop(self):
        root = self.head
        q = [root]
        while q:
            c_node = q.pop(0)
            print(c_node.val)
            # 如果当前节点有下一个节点，则遍历直到最后，否则给下一个赋值
            if c_node.next is None:
                return
            q.append(c_node.next)




if __name__ == '__main__':
    """ __main__ """

    t = Tree()
    t.add(1)
    t.add(2)
    t.add(3)
    t.add(4)
    t.add(5)
    t.add(6)

    t.loop()
    # for i in range(1, 10):
    #     t.add(i)
