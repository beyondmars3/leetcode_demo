def merge_arr():
    """
    合并2个有序的数组
    :return:
    """
    a = [1, 3, 5, 7, 9]
    b = [2, 4, 6, 8, 10]

    res = []
    a_index = 0
    b_index = 0
    if len(a) <= len(b):
        while a_index < len(a):
            if a[a_index] <= b[b_index]:
                res.append(a[a_index])
                a_index += 1
            else:
                res.append(b[b_index])
                b_index += 1

    print(res)


def f(n):
    """
    斐波那契数列--递归写法
    :return:
    """
    if n <= 1:
        return 1

    return f(n - 1) + f(n - 2)


def f1(n):
    """
    生成器的写法
    :param n:
    :return:
    """
    a, b = 0, 1
    while n > 0:
        a, b = b, a + b
        n -= 1
        yield a


def taijie(n):
    """
    一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。
    递归--找到出口--逼近出口
    https://leetcode-cn.com/problems/qing-wa-tiao-tai-jie-wen-ti-lcof/
    :return:
    """
    if n <= 2:
        return n

    return taijie(n - 1) + taijie(n - 2)


def reverse():
    """
    翻转列表--递归
    :return:
    """

    class Node:
        def __init__(self, val):
            self.val = val
            self.next = None

    class Tree:
        def __init__(self):
            self.root = None

        def add(self, val):
            _node = Node(val)
            if self.root is None:
                self.root = _node
                return
            q = [self.root]
            while q:
                c_node = q.pop(0)
                if not c_node.next:
                    c_node.next = _node
                    return
                q.append(c_node.next)

        def loop(self):
            """
            loop
            :return:
            """
            q = [self.root]
            while q:
                c_node = q.pop(0)
                print(c_node.val)
                if not c_node.next:
                    return
                q.append(c_node.next)

    def r_node(head):
        """
        翻转
        :param head:
        :return:
        """
        if not head:
            return None
        if not head.next:
            print(head.val)
            return head

        headNode = r_node(head.next)

        print(headNode.val)

        # head.next.next = head
        # head.next = None

        return headNode

    t = Tree()
    for i in range(1, 10):
        t.add(i)

    # t.loop()
    r_node(t.root)


def f3(n):
    """

    :param n:
    :return:
    """
    print("1")
    if n <= 1:
        return 1
    r = n * f3(n - 1)
    print(r)
    return r


if __name__ == '__main__':
    """ __main__ """

    # reverse()

    abc = f3(6)
    # print(abc)
