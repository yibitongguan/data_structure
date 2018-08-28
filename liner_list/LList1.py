# encoding:utf-8

from LList import LList, LNode, LinkedListUnderflow
from random import randint
"""
含有表头、表尾结点引用域
"""
class LList1(LList):
    def __init__(self):
        super().__init__()
        self._rear = None
        
    def prepend(self, elem):
        if self._head is None:
            self._head = LNode(elem, self._head)
            self._rear = self._head
        else:
            self._head = LNode(elem, self._head)
            
    def append(self, elem):
        if self._head is None:
            self._head = LNode(elem, self._head)
            self._rear = self._head
        else:
            self._rear.next = LNode(elem)
            self._rear = self._rear.next
            
    def pop_last(self):
        if self._head is Node:
            raise LinkedListUnderflow("in pop_last")
        p = self._head
        if p.next is None:
            e = p.elem
            self._head = None
            return e
        while p.next.next:
            p = p.next
        e = p.next.elem
        p.next = None
        self._rear = p
        
if __name__ == '__main__':
    lst = LList()
    for i in range(10):
        lst.prepend(i)
    for i in range(11, 20):
        lst.append(randint(1, 20))
    
    for x in lst.elements():
        print(x, end=',')
    print('')
    for x in lst.filter(lambda y: y % 2 == 0):
        print(x, end=',')
