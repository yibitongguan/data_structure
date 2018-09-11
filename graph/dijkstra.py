# encoding:utf-8

from prioQueue_heap import PrioQueue
from graph import GraphAL

def dijkstra_shortest_paths(graph, v0):
    vnum = graph.vertex_num()
    assert 0 <= v0 < vnum
    paths = [None] * vnum
    count = 0
    # (p, v, v')表示从v0经v到v'的已知最短路径的长度为p
    cands = PrioQueue([(0, v0, v0)])  # 初始队列
    while count < vnum and not cands.is_empty():
        plen, u, vmin = cands.dequeue()  # 取路径最短顶点
        if paths[vmin]:
            continue
        paths[vmin] = (u, plen)  # u为v0到vmin最短路径的前一节点，plen为最短路径距离
        for v, w in graph.out_edges(vmin):
            if not paths[v]:
                cands.enqueue((plen+w, vmin, v))
        count += 1
    return paths
    
if __name__ == '__main__':
    mat = [[0, 0, 5, 2, 0, 0, 0],
            [11, 0, 4, 0, 0, 4, 0],
            [0, 3, 0, 0, 2, 0, 0],
            [0, 0, 0, 0, 6, 0, 0],
            [0, 0, 0, 0, 0, 0, 2],
            [0, 0, 0, 0, 0, 0, 3],
            [0, 0, 0, 0, 0, 0, 0]]
    g = GraphAL(mat)
    print(dijkstra_shortest_paths(g, 0))
