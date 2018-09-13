# encoding:utf-8
"""
@author = Dcm
@create_time = 2018/9/12 23:17
"""
from dictBinTree import DictBinTree
from avlNode import AVLNode
from assoc import Assoc

# 用AVL树类实现字典
class DictAVL(DictBinTree):
    def __init__(self):
        super().__init__()

    # LL调整
    @staticmethod
    def LL(a, b):
        a.left = b.right
        b.right = a
        a.bf = b.bf = 0
        return b

    # RR调整
    @staticmethod
    def RR(a, b):
        a.left = b.right
        b.right = a
        a.bf = b.bf = 0
        return b

    # LR调整
    @staticmethod
    def LR(a, b):
        c = b.right
        a.left, b.right = c.right, c.left
        c.left, c.right = b, a
        if c.bf == 0:          # c本身就是插入节点
            a.bf = b.bf = 0
        elif c.bf == 1:        # 新结点在c的左子树
            a.bf = -1
            b.bf = 0
        else:                  # 新结点在c的右子树
            a.bf = 0
            b.bf = 1
        c.bf = 0
        return c

    # RL调整
    @staticmethod
    def RL(a, b):
        c = b.right
        a.right, b.left = c.left, c.right
        c.left, c.right = a, b
        if c.bf == 0:          # c本身就是插入节点
            a.bf = b.bf = 0
        elif c.bf == 1:        # 新结点在c的左子树
            a.bf = 0
            b.bf = -1
        else:                  # 新结点在c的右子树
            a.bf = -1
            b.bf = 0
        c.bf = 0
        return c

    # 插入操作
    def insert(self, key, value):
        a = p = self._root
        if a is None:
            self._root = AVLNode(Assoc(key, value))
            return
        pa = q = None                # 维持pa, q为a, p的父节点
        while p:                     # 确定插入位置和最小非平衡子树
            if key == p.data.key:
                p.data.value = value
                return
            if p.bf != 0:
                pa, a = q, p
            q = p
            if key < p.data.key:
                p = p.left
            else:
                p = p.right
        node = AVLNode(Assoc(key, value))
        # q是插入点的父节点
        if key < q.data.key:
            q.left = node
        else:
            q.right = node
        # 新结点已插入
        if key < a.data.key:        # 新结点在a的左子树
            p = b = a.left
            d = 1                   # d记录新结点在a的哪颗子树
        else:
            p = b = a.right         # 新结点在a的右子树
            d = 1
        # 修改b到新结点路径上各节点的BF值，b为a的子节点
        while p != node:
            if key < p.data.key:    # p的左子树增高
                p.bf = 1
                p = p.left
            else:                   # p的右子树增高
                p.bf = -1
                p = p.right
        if a.bf == 0:
            a.bf = d
            return
        if a.bf == -d:               # 新结点在较低子树里
            a.bf = 0
            return
        # 新结点在较高子树，失衡
        if d == 1:                    # 新结点在a的左子树
            if b.bf == 1:
                b = DictAVL.LL(a, b)  # LL调整
            else:
                b = DictAVL.LR(a, b)  # LR调整
        else:                         # 新结点在a的右子树
            if b.bf == -1:
                b = DictAVL.RR(a, b)  # RR调整
            else:
                b = DictAVL.RL(a, b)  # RL调整
        if pa is None:                # 原a为树根，修改_root
            self._root = b
        else:                         # a为非树根
            if pa.left == a:
                pa.left = b
            else:
                pa.right = b
