# encoding:utf-8
"""
@author = Dcm
@create_time = 2018/9/5 23:47
"""
from prioQueue_heap import PrioQueue
from binTNode import BinTNode

class HTNode(BinTNode):
    def __lt__(self, other):
        return self.data < other.data

class HuffmanPrioQ(PrioQueue):
    # 检查队列元素个数
    def number(self):
        return len(self._elems)

# 构造哈夫曼树
def HuffmanTree(weights):
    trees = HuffmanPrioQ()
    for w in weights:
        trees.enqueue(HTNode(w))
    while trees.number() > 1:
        t1 = trees.dequeue()
        t2 = trees.dequeue()
        x = t1.data + t2.data
        trees.enqueue(HTNode(x, t1, t2))
    return trees.dequeue()
