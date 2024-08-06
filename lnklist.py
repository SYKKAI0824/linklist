class Node:
    def __init__(self,data,_next = None):
        self.data = data
        self.next = _next

class Singlecyclelinklist:
    def __init__(self,head = None,lenth = 0):
        self.head = head
        self.lenth = lenth

    def is_empty(self):
        return self.lenth == 0

    def _lenth(self):
        return self.lenth

    def nodes_list(self):
        '''
        跟单项链表中不一样  因为单向链表中  有值为None的指针域
        但是单向循环链表中没有None
        :return:
        '''

        # 自己写的代码
        res = []
        cur = self.head   # 第一个结点
        b = ''
        while cur and b != self.head:
            res.append(cur.data)
            cur= cur.next
            b = cur
        return res

    def add(self,data):
        # 在链表的头部添加一个结点
        '''
        新建一个结点
        新节点的指针域指向原来的头节点
        尾结点的指针域指向新的结点
        head指针域指向新的结点
        :param data:
        :return:
        '''
        node = Node(data)
        if self.is_empty():
            self.head = node
            node.next = self.head
        else:
            node.next = self.head
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = node
            self.head = node
        self.lenth += 1

    def append(self,data):
        # 往链表的尾部添加一个节点
        '''
        1. 创建一个新的结点node
        2. 将新节点node的指针域指向头节点（self.head）
        3. 找到原来的尾结点
        4. 将原来尾结点的指针指向新的结点
        5. 长度加 1
        :param data:
        :return:
        '''
        node = Node(data)
        if self.head:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = node
        else:
            self.head = node
        node.next = self.head
        self.lenth += 1

    def insert(self,pos,data):
        # 给链表中指定的位置添加结点
        '''
        创建新的结点node
        循环找到pos-1位置上 的结点 命名为cur
        将新的结点的next属性指向pos-1结点的next
        原来该位置的结点的前置结点的next属性指向新的结点node
        长度+1
        :param pos:
        :param data:
        :return:
        '''


        if pos <= 0:          # 必须加等号
            self.add(data)
        elif pos > self.lenth:    # 加不加等号无所谓
            self.append(data)
        else:
            node = Node(data)
            cur = self.head
            a = pos - 1
            while a:
                cur = cur.next
                a -= 1
            node.next = cur.next
            cur.next = node
        self.lenth += 1

    def remove_pos(self,pos):
        # 删除索引为pos的结点
        '''
        正常情况下：
        循环遍历找到pos结点和前驱结点
        将前驱结点的  next属性指向pos结点的next属性
        长度-1
        特殊情况
        if 为 头节点 pos = 0
        直接将self.head = 头节点的next
        if 为 尾部结点
        执行上述的命令应该可以
        :param pos:
        :param data:
        :return:
        '''
        if not pos:
            self.head = self.head.next
        elif pos >= self.lenth or pos < 0:
            print('索引不在范围内')
        else:
            cur = self.head
            prev = None
            while pos:
                prev = cur
                cur = cur.next
                pos -= 1
            prev.next = cur.next

    def remove_My(self, data):
        # 删除第一个值为data的结点
        '''
        首先判断链表是否为空
        正常情况下
        循环遍历每一个结点  遍历次数为lenth-1次
        找到值为data的结点
        将该节点的next属性赋值给前驱结点的next属性
        长度-1
        :param data:
        :return:
        '''
        cur = self.head
        a = self.lenth
        prev = None
        while a:                         # 进去 self.lenth - 1次，出来后，刚好将cur放到尾结点处 但是此时不让进了 就很遗憾
            if cur.data == data:
                if not prev:
                    while cur.next != self.head:
                        cur = cur.next
                    self.head = self.head.next    # 必须放在while循环后面  因为while循环中会用到参数  不可修改
                    cur.next = self.head
                else:
                    prev.next = cur.next
                self.lenth -= 1
                return 0
            prev = cur
            cur = cur.next
            a -= 1
        return -1

    def remove(self,data):
        # 删除第一个值为data的结点
        if self.is_empty():
            return -1
        cur = self.head
        flag = True
        prev = None
        while cur != self.head or flag:
            flag = False
            if cur.data == data:
                if not prev:
                    last_node = self.head
                    while last_node.next != self.head:
                        last_node = last_node.next
                    self.head = self.head.next
                    last_node.next = cur.next
                else:
                    prev.next = cur.next
                self.lenth -= 1
                return 0
            prev = cur
            cur = cur.next
        return -1

    def modify(self,pos,data):
        # 修改链表中指定位置的值
        '''
        正常情况下
        循环遍历找到指定位置的值  （例如pos = 2   循环进行两次）
        将结点的data属性指向新的data
        如果输入的pos超出范围
        :param pos:
        :return:
        '''
        if 0 <= pos < self.lenth:
            cur = self.head
            while pos:
                cur = cur.next
                pos -= 1
            cur.data = data
        else:
            print('索引超出范围')

    def search(self,data):
        '''
        查找链表中是否有值为data的结点
        循环遍历每一个结点  两种遍历方法（详见remove的两种方法）
        判断是否data属性的值为data
        有  T  没有  F
        此外  判断链表是否为空值（本次采用的remove循环不需要判断，但是要注意循环的次数，即找到了尾部结点之后需不需要重新进入循环？！！！）
        :param data:
        :return:
        '''
        cur = self.head
        a = self.lenth
        while a:
            if cur.data == data:
                return True
            cur = cur.next
            a -= 1
        return False

if __name__ == '__main__':
    l1 = Singlecyclelinklist()
    l1.add(11)
    l1.add(2)
    l1.add(1)
    l1.add(2)
    l1.add(1)
    l1.add(2)
    print(l1.nodes_list())
    print(l1.search(1))
