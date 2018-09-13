# encoding:utf-8
"""
@author = Dcm
@create_time = 2018/9/12 23:13
"""
from binTNode import BinTNode

# AVL树结点类
class AVLNode(BinTNode):
    def __init__(self, data):
        super().__init__(data)
        self.bf = 0  # 结点的平衡因子