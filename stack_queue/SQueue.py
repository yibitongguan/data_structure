# encoding：utf-8

# 定义异常
class QueueUnderflow(ValueError):
    pass
    
"""
队列类
"""
class SQueue:
    def __init__(self, init_len=8):
        self._len = init_len           # 存储区长度，初始为8
        self._elems = [0] * init_len   # 元素存储
        self._head = 0                 # 表头元素下标
        self._num = 0                  # 元素个数
        
    def is_empty(self):
        return self._num == 0
    
    # 读取队列头的值    
    def peek(self):
        if self._num == 0:
            raise QueueUnderflow
        return self._elems[self._head]
    
    # 出队列    
    def dequeue(self):
        if self._num == 0:
            raise QueueUnderflow
        e = self._elems[self._head]
        self._head = (self._head + 1) % self._len
        self._num -= 1
        return e
    
    # 入队列    
    def enqueue(self, e):
        if self._num == self._len:
            self.__extend()
        self._elems[(self._head + self._num) % self._len] = e
        self._num += 1
    
    # 扩充存储区        
    def __extend(self):
        old_len = self._len
        self._len *= 2       # 存储区长度加倍
        new_elems = [0] * self._len
        for i in range(old_len):
            new_elems[i] = self._elems[(self._head + i) % old_len]
        self._elems, self._head = new_elems, 0            
