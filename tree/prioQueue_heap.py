# encoding:utf-8

from prioQueue_list import PrioQueueError
"""
基于堆实现优先队列
"""

class PrioQueue:
    def __init__(self, elist=[]):
        self._elems = list(elist)
        if elist:
            self.buildheap()
            
    def is_empty(self):
        return not self._elems
        
    def peek(self):
        if self.is_empty():
            raise PrioQueueError("in peek")
        return self._elems[0]
        
    def enqueue(self, e):
        self._elems.append(None)
        self.siftup(e, len(self._elems)-1)
    
    # 向上筛选    
    def siftup(self, e, last):
        elems, i, j = self._elems, last, (last-1)//2
        while i > 0 and e < elems[j]:
            elems[i] = elems[j]
            i, j = j, (j-1)//2
        elems[i] = e
        
    def dequeue(self):
        if self.is_empty():
            raise PrioQueueError("in dequeue")
        elems = self._elems
        e0 = elems[0]
        e = elems.pop()  # 弹出最后元素
        if len(elems) > 0:
            self.siftdown(e, 0, len(elems))
        return e0
        
    # 向下筛选
    def siftdown(self, e, begin, end):
        elems, i, j = self._elems, begin, begin*2+1
        while j < end:
            if j+1 < end and elems[j+1] < elems[j]:
                j += 1             # elems[j]不大于其兄弟节点的数据
            if e < elems[j]:       # e在三者中最小，已找到位置
                break
            elems[i] = elems[j]    # elems[j]在三者中最小，上移
            i, j = j, 2*j+1
        elems[i] = e
    
    # 构建初始堆    
    def buildheap(self):
        end = len(self._elems)
        for i in range(end//2, -1, -1):
            self.siftdown(self._elems[i], i, end)
