# encoding:utf-8
"""
@author = Dcm
@create_time = 2018/9/6 23:35
"""
from graph import GraphAL
from prioQueue_heap import PrioQueue

"""
prim算法求最小生成树
"""
def Prim(graph):
    vnum = graph.vertex_num()
    mst = [None] * vnum
    cands = PrioQueue([(0, 0, 0)])  # 记录候选边
    count = 0
    while count < vnum and not cands.is_empty():
        w, u, v = cands.dequeue()  # 取最短边
        if mst[v]:
            continue
        mst[v] = ((u, v), w)
        count += 1
        for vi, w in graph.out_edges(v):
            if not mst[vi]:  # 如果vi不在mst则这条边是侯选边
                cands.enqueue((w, v, vi))
    return mst

if __name__ == '__main__':
    mat = [[0, 5, 11, 5, 0, 0, 0],
           [5, 0, 0, 3, 9, 0, 7],
           [11, 0, 0, 7, 0, 6, 0],
           [5, 3, 7, 0, 0, 0, 20],
           [0, 9, 0, 0, 0, 0, 8],
           [0, 0, 6, 0, 0, 0, 8],
           [0, 7, 0, 20, 8, 8, 0]]
    g = GraphAL(mat)
    print(Prim(g))
