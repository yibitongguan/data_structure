# encoding:utf-8
"""
@author = Dcm
@create_time = 2018/9/6 21:40
"""
from graph import Graph

def DFS_span_forest(graph):
    vnum = graph.vertex_num()
    span_forest = [None] * vnum

    def dfs(graph, v):
        nonlocal span_forest
        for u, w in graph.out_edges(v):
            if span_forest[u] is None:
                # 序对(vj, e)，其中vj是从v0到vi路径上vi的前一节点，
                # e是vj到vi的邻接边的信息
                span_forest[u] = (v, w)
                dfs(graph, u)
    for v in range(vnum):
        if span_forest[v] is None:
            span_forest[v] = (v, 0)
            dfs(graph, v)
    return span_forest

if __name__ == '__main__':
    mat = [[0, 0, 6, 3, 0, 0, 0],
           [11, 0, 4, 0, 0, 7, 0],
           [0, 3, 0, 0, 5, 0, 0],
           [0, 0, 0, 0, 5, 0, 0],
           [0, 0, 0, 0, 0, 0, 9],
           [0, 0, 0, 0, 0, 0, 10],
           [0, 0, 0, 0, 0, 0, 0]]
    g = Graph(mat)
    print(DFS_span_forest(g))
