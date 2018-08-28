# encoding:utf-8

from LList import LNode, LinkedListUnderflow
from LList1 import LList1

"""
双链表结点
"""
class DLNode(LNode):
    def __init__(self, elem, prev=None, next_=None):
        super().__init__(elem, next_)
        self.prev = prev

"""
双链表类
"""
class DLList(LList1):
    def __init__(self):
        super().__init__()
        
    def prepend(self, elem):
        p = DLNode(elem, None, self._head)
        if self._head is None:
            self._rear = p
        else:
            p.next.prev = p
        self._head = p
        
    def append(self, elem):
        p = DLNode(elem, self._rear, None)
        if self._head is None:
            self._head  = p
        else:
            p.prev.next = p
        self._rear = p
        
    def pop(self):
        if self._head is None:
            raise LinkedListUnderflow("in pop of DLList")
        e = self._head.elem
        self._head = self._head.next
        if self._head:
            self._head = None
        return e
        
    def pop_last(self):
        if self._head is None:
            raise LinkedListUnderflow("in pop_last of DLList")
        e = self._rear.elem
        self._rear = self._rear.prev
        if self._rear is None:
            self._head = None
        else:
            self._rear.next = None
        return e

if __name__ == '__main__':
    lst = DLList()
    for i in range(10):
        lst.prepend(i)
    
    for x in lst.elements():
        print(x, end=',')
    print('')
    for x in lst.filter(lambda y: y % 2 == 0):
        print(x, end=',')
