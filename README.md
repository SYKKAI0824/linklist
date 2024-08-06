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

![01]()

                        


