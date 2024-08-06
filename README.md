# 结构
单向循环链表将尾结点的指针域指向头节点，常用于丢手绢之类的循环问题中
结构图如下：
![01](https://github.com/SYKKAI0824/linklist/blob/c65cbeaffe986e7e2bd47ccce79f73e2c5603a74/01.png)

单向循环链表具体的操作

![01](https://github.com/SYKKAI0824/linklist/blob/0bace8ed7276dfef3634a4a6a8ceabc491ce1284/02.png)

判断链表是否为空
```
class None:
   def __init__(self,data,_next):
       self.data = data
       self.next = _next

class Singlecyclelinklist:
   def __init__(self,head,lenth):
       self.head = None
       self.lenth = 0

   def is_empty(self):
       return self.lenth == 0

   def _lenth(self):
       return self.lenth
```

添加头结点

![01](https://github.com/SYKKAI0824/linklist/blob/e3d42d6358b8a3bfa67d037b4573c057f0ac28eb/03.png)

```
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
            while cur.next != self.head:  # 默认有结点
                cur = cur.next
            cur.next = node
            self.head = node
        self.lenth += 1
```                    

将链表中的所有的数据装到列表中
方法1
```
    def nodes_list(self):
        # 返回链表中的所有节点的值组成的列表
        res = []
        if self.is_empty():
            return res
        res.append(self.head.data)  #添加头节点
        cur = self.head.next  # 第二个结点
        while cur != self.head:
            res.append(cur.data)
            cur = cur.next
        return res

```
方法二
```
    def nodes_list(self):
        # 返回链表中的所有节点的值组成的列表
        res = []
        if self.is_empty():
            return res
        res.append(self.head.data)  #添加头节点
        cur = self.head.next  # 第二个结点
        while cur != self.head:
            res.append(cur.data)
            cur = cur.next
        return res

```
错误方法
```
    def nodes_list2(self):
        res = []
        if self.is_empty():
            return res
        cur = self.head
        while cur.next != self.head:    # 下一个结点判断
            res.append(cur.data)        # 当前结点添加数据
            cur = cur.next
        return res

```
注意这行代码在进行循环的时候，是将下一个节点作为循环条件，将当前节点进行添加到列表，故当最后一个结点满足条件的时候，最后一个节点不会进入循环，故会少最后一个结点

往链表的尾部添加一个节点

```
    def append(self,data):
        # 往链表的尾部添加一个节点
        '''
        1. 创建一个新的结点node
        2. 将新节点node的指针域指向头节点（self.head）
        3. 找到原来的尾结点
        4. 将原来尾结点的指针指向新的结点
        5. 长度加1
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
        self.lenth += 1

```
```
'''
优化代码
        node.next = self.head  两句都有  直接拉出来放到一行
        if self.head:
        if判断条件  能不调用就不调用
'''
	def append(self,data):
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

```
往链表中的指定位置插入结点

![01](https://github.com/SYKKAI0824/linklist/blob/e3d42d6358b8a3bfa67d037b4573c057f0ac28eb/04.png)

```
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


        if pos <= 0:              # 必须加等号
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

```

删除链表中第一个值为data的结点

![01](https://github.com/SYKKAI0824/linklist/blob/e3d42d6358b8a3bfa67d037b4573c057f0ac28eb/05.png)

方法一
```
    def remove_My(self, data):
        # 删除第一个值为data的结点
        '''
        正常情况下
        循环遍历每一个结点  遍历次数为lenth-1次
        找到值为data的结点
        将该节点的next属性赋值给前驱结点的next属性
        长度-1
        :param data:
        :return:
        '''
        '''
        在本行代码中不用判断是否为空值  因为以下代码的循环条件是长度即循环的次数是固定的
        if self.is_empty():
            return -1
        '''
        cur = self.head
        a = self.lenth
        prev = None
        while a:   # 进去 self.lenth - 1次，出来后，刚好将cur放到尾结点处 但是此时不让进了 就很遗憾
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

```
方法二
与方法1的区别在于该方法的循环是在节点本身的基础上进行的，前者是在长度的基础上进行的
```
    def remove(self,data):
        # 删除第一个值为data的结点
        if self.is_empty():
            return -1
        cur = self.head
        flag = True   # 创建一个标志位保证在循环进行的时候第一个结点一定能够进入循环
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


```
修改链表中指定位置的值
理应来讲指定位置的值的修改，并不会影响链表本身的结构，故跟单向链表的方法是一样的
```
    def modify(self,pos,data):   # 与单向链表相同
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

```
查找链表中是否有结点的值为data

```
    def search(self,data):
        '''
        查找链表中是否有值为data的结点
        循环遍历每一个结点  两种遍历方法（详见remove的两种方法）
        判断是否data属性的值为data
        有  T  没有  F
        此外  判断链表是否为空值（本次采用的remove方法1循环不需要判断，但是要注意循环的次数，即找到了尾部结点之后需不需要重新进入循环？！！！）
        '''
        cur = self.head
        a = self.lenth
        while a:
            if cur.data == data:
                return True
            cur = cur.next
            a -= 1
        return False
'''
升级版本=====>>>>>>返回data所在的索引
'''

```
删除指定位置的结点
```
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

```
单向循环链表的代码时间复杂度的优化
时间复杂度复杂在那里呢？

每次查找尾部节点的时候都会遍历循环整个链表（复杂在这里）

如何进行解决呢？

在初始化方法中定义第三个参数last_node = None

```
class Singlecyclelinklist:
    def __init__(self,head = None,lenth = 0，last_node = None):
        self.head = head
        self.lenth = lenth
        self.last_node = last_node    # 这里这里看这里
'''
下面的代码就交给小伙伴自行进行补充喽
'''

```

