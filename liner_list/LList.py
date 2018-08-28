# encoding:utf-8
"""
@author = Dcm
@create_time = 2018/8/27 22:10
"""
from random import randint
"""
链表节点
"""
class LNode:
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_

# 定义链表异常
class LinkedListUnderflow(ValueError):
    pass

"""
单链表
"""
class LList:
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    # 表头插入数据
    def prepend(self, elem):
        self._head = LNode(elem, self._head)

    # 删除表头结点
    def pop(self):
        if self._head is None:  # 表中无节点，引发异常
            raise LinkedListUnderflow("in pop")
        e = self._head.elem
        self._head = self._head.next
        return e

    # 表尾插入数据
    def append(self, elem):
        if self._head is None:
            self._head = LNode(elem)
            return
        p = self._head
        while p.next:
            p = p.next
        p.next = LNode(elem)

    # 删除表尾节点
    def pop_last(self):
        if self._head is None:  # 空表
            raise LinkedListUnderflow("in pop_last")
        p = self._head
        if p.next is None:  # 表中只有一个元素
            e = p.elem
            self._head = None
            return e
        while p.next.next:
            p = p.next
        e = p.next.elem
        p.next = None
        return e

    # 迭代生成器
    def elements(self):
        p = self._head
        while p:
            yield p.elem
            p = p.next

    # 过滤生成器
    def filter(self, pred):
        p = self._head
        while p:
            if pred(p.elem):
                yield p.elem
            p = p.next
            
    # 链表反转
    def rev(self):
        p = None
        while self._head:
            q = self._head
            self._head = q.next  # 摘下原来的首结点
            q.next = p
            p = q                 # 将刚摘下的结点加入p引用的结点序列
        self._head = p            # 重置表头链接
    
    # 移动表中元素实现插入排序
    def sort1(self):
        if self._head is None:
            return
        crt = self._head.next          # 从首结点之后开始处理
        while crt:
            x = crt.elem 
            p = self._head
            while p is not crt and p.elem <= x:  # 跳过小元素
                p = p.next
            while p is not crt:         # 倒换大元素，完成元素插入的工作
                y = p.elem 
                p.elem = x
                x = y
                p = p.next
            crt.elem = x   # 回填最后一个元素
            crt = crt.next
    
    # 调整链接方式实现插入排序
    def sort(self):
        p = self._head
        if p is None or p.next is None:
            return
            
        rem = p.next
        p.next = None
        while rem is not None:
            p = self._head
            q = None
            while p and p.elem <= rem.elem:
                q = p
                p = p.next
            if q is None:
                self._head = rem
            else:
                q.next = rem
            q = rem
            rem = rem.next
            q.next = p

if __name__ == '__main__':
    lst = LList()
    for i in range(10):
        lst.prepend(i)
    
    #lst.rev()
    
    for i in range(11, 20):
        lst.append(randint(1, 20))
    
    #lst.sort1()
    lst.sort()
    
    for x in lst.elements():
        print(x, end=',')
    print('')
    for x in lst.filter(lambda y: y % 2 == 0):
        print(x, end=',')
