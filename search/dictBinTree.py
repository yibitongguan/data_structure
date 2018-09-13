# encoding:utf-8

from assoc import Assoc
from binTNode import BinTNode
from SStack import SStack

# 二叉排序树实现字典
class DictBinTree:
    def __init__(self):
        self._root = None
        
    def is_empty(self):
        return self._root is None
    
    # 检索    
    def search(self, key):
        bt = self._root
        while bt is not None:
            entry = bt.data
            if key < entry.key:
                bt = bt.left
            elif key > entry.key:
                bt = bt.right
            else:
                return entry.value
        return None
    
    # 插入    
    def insert(self, key, value):
        bt = self._root
        if bt is None:
            self._root = BinTNode(Assoc(key, value))
            return
        while True:
            entry = bt.data
            if key < entry.key:
                if bt.left is None:
                    bt.left = BinTNode(Assoc(key, value))
                    return
                bt = bt.left
            elif key > entry.key:
                if bt.right is None:
                    bt.right = BinTNode(Assoc(key, value))
                    return
                bt = bt.right
            else:
                bt.data.value = value
                return
                
    def values(self):
        t, s = self._root, SStack()
        while t or not s.is_empty():
            while t:
                s.push(t)
                t = t.left
            t = t.pop()
            yield t.data.value
            t = t.right
            
    def entries(self):
        t, s = self._root, SStack()
        while t or not s.is_empty():
            while t:
                s.push(t)
                t = t.left
            t = s.pop()
            yield t.data.key, t.data.value
            t = t.right
    
    # 删除        
    def delete(self, key):
        p, q = None, self._root  # 维持p为q的父节点
        while q and q.data.key != key:
            p = q
            if key < q.data.key:
                q = q.left
            else:
                q = q.right
            if q is None:
                return
                
            if q.left is None:  # 如果q没有左子节点
                if p is None:  # q是根节点
                    self._root = q.right
                elif q is p.left:
                    p.left = q.right
                else:
                    p.right = q.right
                return
                
            r = q.left  # 找q左子树的最右结点
            while r.right is not None:
                r = r.right
            r.right = q.right
            if p is None:  # q是根节点, 修改_root
                self._root = q.left
            elif p.left is q:
                p.left = q.left
            else:
                p.right = q.left
                
    def print(self):
        for k, v in self.entries():
            print(k, v)
            
def build_dictBinTree(entries):
    dic = DictBinTree()
    for k, v in entries:
        dic.insert(k, v)
    return dic

if __name__ == '__main__':
    entries = [('a', 100), ('c', 10), ('b', 1)]
    dic = build_dictBinTree(entries)
    dic.print()
