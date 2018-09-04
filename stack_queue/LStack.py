# encoding:utf-8

from linear_list.LList import LNode
from SStack import StackUnderflow

# 基于链表实现的栈类，用LNode作为结点, 链的头部作为栈顶
class LStack():
    def __init__(self):
        self._top = None
        
    def is_empty(self):
        return self._top is None
        
    def top(self):
        if self._top is None:
            raise StackUnderflow("in LStack.top()")
        return self._top.elem
        
    def push(self, elem):
        self._top = LNode(elem, self._top)
        
    def pop(self):
        if self._top is None:
            raise StackUnderflow("in LStack.pop()")
        p = self._top
        self._top = p.next
        return p.elem

if __name__ == '__main__':
    st1 = SStack()
    st1.push(3)
    st1.push(5)
    while not st1.is_empty():
        print(st1.pop())
