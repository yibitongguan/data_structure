# encoding:utf-8
"""
@author = Dcm
@create_time = 2018/9/5 21:22
"""
from SQueue import SQueue
from SStack import SStack
"""
二叉树结点类
"""
class BinTNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

# 统计树中节点个数
def count_BinTNodes(t):
    if t is None:
        return 0
    else:
        return 1 + count_BinTNodes(t.left) + count_BinTNodes(t.right)

# 求二叉树里所有数值和
def sum_BinTNode(t):
    if t is None:
        return 0
    else:
        return t.data + sum_BinTNode(t.left) + sum_BinTNode(t.right)

# 先序遍历递归函数
def preorder(t, proc):
    if t is None:
        return
    proc(t.data)
    preorder(t.left, proc)
    preorder(t.right, proc)

# 宽度优先遍历
def levelorder(t, proc):
    qu = SQueue()
    qu.enqueue(t)
    while not qu.is_empty():
        t = qu.dequeue()
        if t is None:
            continue
        if t.left:
            qu.enqueue(t.left)
        if t.right:
            qu.enqueue(t.right)
        proc(t.data)

# 非递归先序遍历
def preorder_nonrec(t, proc):
    s = SStack()
    while t is not None or not s.is_empty():
        while t:
            proc(t.data)
            s.push(t.right)  # 右分支入栈
            t = t.left
        t = s.pop()  # 遇到空树，回溯

# 二叉树迭代器
def preorder_elements(t):
    s = SStack()
    while t is not None or not s.is_empty():
        while t:
            s.push(t.right)  # 右分支入栈
            yield t.data
            t = t.left
        t = s.pop()  # 遇到空树，回溯

# 非递归后序遍历
def postorder_nonrec(t, proc):
    s = SStack()
    while t or not s.is_empty():
        while t:  # 下行循环，直到栈顶的两子树空
            s.push(t)
            t = t.left if t.left else t.right  # 能左就左，否则向右
        t = s.pop()  # 栈顶是应访问节点
        proc(t.data)
        if not s.is_empty() and s.top().left == t:
            t = s.top().right
        else:
            t = None

if __name__ == '__main__':
    t = BinTNode(1, BinTNode(2, BinTNode(5)), BinTNode(3))
    print(count_BinTNodes(t))
    print(sum_BinTNode(t))
    # preorder(t, lambda x: print(x, end=" "))
    # levelorder(t, lambda x: print(x, end=" "))
    # preorder_nonrec(t, lambda x: print(x, end=" "))
    # for i in preorder_elements(t):
    #     print(i)
    postorder_nonrec(t, lambda x: print(x, end=" "))
