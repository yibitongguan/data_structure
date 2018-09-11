# encoding:utf-8

# AOV网的拓扑排序
def toposort(graph):
    vnum = graph.vertex_num()
    indegree, toposeq = [0] * vnum, []
    zerov = -1
    for vi in range(vnum):  # 建立初始的入度表
        for v, w in graph.out_edges(vi):
            indegree[v] += 1
    for vi in range(vnum):
        if indegree[vi] == 0:  # 建立初始的0度表
            indegree[vi] = zerov
            zerov = vi
    for n in range(vnum):
        if zerov == -1:  # 不存在拓扑序列
            return False
        vi = zerov
        zerov = indegree[zerov]  # 从0度表弹出顶点vi
        toposeq.append(vi)  # 把一个vi加入拓扑序列
        for v, w in graph.out_edges(vi):  # 检查vi的出边
            indegree[v] -= 1
            if indegree[v] == 0:
                indegree[v] == zerov
                zerov = v
    return toposeq


