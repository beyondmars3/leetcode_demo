class Node:

    def __init__(self, data, left=None, right=None):
        self.left = left
        self.right = right
        self.data = data


class Tree:

    def __init__(self, val=None):
        self.root = val

    def add(self, d):
        """
        从上到下，从左到右
        :param d:
        :return:
        """
        _node = Node(d)
        if not self.root:
            self.root = _node

        q = list()
        q.append(self.root)

        while q:
            c = q.pop(0)
            # print(c.data)
            if not c.left:
                c.left = _node
                return

            if not c.right:
                c.right = _node
                return

            q.append(c.left)
            q.append(c.right)

    def g(self):
        """
        上-下， 左-右
        :return:
        """

        q = list()
        q.append(self.root)

        while q:
            c = q.pop(0)
            res = "root: {}".format(c.data)
            print(res)

            if not all([c, c.left, c.right]):
                return

            if c.left:
                q.append(c.left)

            if c.left:
                q.append(c.right)


if __name__ == '__main__':
    """ __main__ """

    t = Tree()
    for i in range(1, 10):
        t.add(i)

    t.g()