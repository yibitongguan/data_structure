# encoding:utf-8
"""
@author = Dcm
@create_time = 2018/9/12 21:49
"""
from dictBinTree import DictBinTree
from assoc import Assoc
from binTNode import BinTNode

# 最佳二叉排序树
class DictOptBinTree(DictBinTree):
    def __init__(self, seq):
        super().__init__()
        data = sorted(seq)
        self._root = DictBinTree.buildOBT(data, 0, len(data) - 1)

    @staticmethod
    def buildOBT(data, start, end):
        if start > end:
            return None
        mid = (end + start) // 2
        left = DictOptBinTree.buildOBT(data, start, mid - 1)
        right = DictOptBinTree.buildOBT(data, mid + 1, end)
        return BinTNode(Assoc(*data[mid]), left, right)
