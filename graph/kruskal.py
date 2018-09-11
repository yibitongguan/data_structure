# encoding:utf-8
"""
@author = Dcm
@create_time = 2018/9/6 22:36
"""
from graph import GraphAL

"""
kruskal算法求最小生成树
"""
def Kruskal(graph):
    vnum = graph.vertex_num()
    reps = [i for i in range(vnum)]  # 记录各个顶点是否是连通的
    mst, edges = [], []
    for vi in range(vnum):
        for v, w in graph.out_edges(vi):
            edges.append((w, vi, v))  # 添加边信息
    edges.sort()  # 按边的权值排序
    for w, vi, vj in edges:
        if reps[vi] != reps[vj]:  # 边的两端点属于不同连通分量
            mst.append(((vi, vj), w))
            if len(mst) == vnum - 1:
                break
            rep, orep = reps[vi], reps[vj]
            for i in range(vnum):  # 合并连通分量，统一代表元
                if reps[i] == orep:
                    reps[i] = rep
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
    print(Kruskal(g))
