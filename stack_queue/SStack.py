# encoding:utf-8

# 定义异常
class StackUnderflow(ValueError):  # 栈下溢（空栈访问）
    pass
    
"""
使用python中的list模拟栈
用一个list类型的数据属性_elems作为栈元素存储区
把_elems的首端作为栈底，尾端作为栈顶
"""
class SStack():
    def __init__(self):
        self._elems = []
        
    def is_empty(self):
        return self._elems == []
        
    def top(self):
        if self._elems == []:
            raise StackUnderflow("in SStack.top()")
        return self._elems[-1]
        
    def push(self, elem):
        self._elems.append(elem)
        
    def pop(self):
        if self._elems == []:
            raise StackUnderflow("in SStack.pop()")
        return self._elems.pop()

if __name__ == '__main__':
    st1 = SStack()
    st1.push(3)
    st1.push(5)
    while not st1.is_empty():
        print(st1.pop())
