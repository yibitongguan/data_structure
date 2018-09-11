# encoding:utf-8

inf = float("inf")  # inf的值大于任何float类型的值

class GraphError(ValueError):
    pass

"""
基本图类，采用邻接矩阵表示
"""
class Graph:
    def __init__(self, mat, unconn=0):  # mat是一个二维的表参数
        vnum = len(mat)
        for x in mat:
            if len(x) != vnum:  # 检查是否为方阵
                raise ValueError("Argument for 'Graph'.")
        self._mat = [mat[i][:] for i in range(vnum)]  # 拷贝
        self._unconn = unconn  # 无关联情况提供的一个特殊值
        self._vnum = vnum  # 顶点个数
        
    def vertex_num(self):
        return self._vnum
        
    def _invalid(self, v):
        return 0 > v or v >= self._vnum
        
    def add_vertex(self):  # 不支持
        pass
        
    def add_edge(self, vi, vj, val=1):
        if self._invalid(vi) or self._invalid(vj):
            raise GraphError(str(vi) + 'or' + str(vj) + "is not a valid vertex")
        self._mat[vi][vj] = val
        
    def get_edge(self, vi, vj):
        if self._invalid(vi) or self._invalid(vj):
            raise GraphError(str(vi) + 'or' + str(vj) + "is not a valid vertex")
        return self._mat[vi][vj]
        
    def out_edges(self, vi):
        if self._invalid(vi):
            raise GraphError(str(vi) + "is not a valid vertex")
        return self._out_edges(self._mat[vi], self._unconn)
        
    @staticmethod
    def _out_edges(row, unconn):
        edges = []
        for i in range(len(row)):
            if row[i] != unconn:
                edges.append((i, row[i]))
        return edges
        
    def __str__(self):
        return "[\n" + ",\n".join(map(str, self._mat)) + "\n]" \
                + "\nUnconnected: " + str(self._unconn)
        
"""
邻接表实现
"""       
class GraphAL(Graph):
    def __init__(self, mat=[], unconn=0):
        vnum = len(mat)
        for x in mat:
            if len(x) != vnum:  # 检查是否为方阵
                raise ValueError("Argument for 'GraphAL'.")
        self._mat = [Graph._out_edges(mat[i], unconn) for i in range(vnum)]
        self._unconn = unconn  # 无关联情况提供的一个特殊值
        self._vnum = vnum  # 顶点个数
        
    def add_vertex(self):
        self._mat.append([])
        self._vnum += 1
        return self._vnum
        
    def add_edge(self, vi, vj, val=1):
        if self._vnum == 0:
            raise GraphError("cannot add edge to empty graph")
        if self._invalid(vi) or self._invalid(vj):
            raise GraphError(str(vi) + 'or' + str(vj) + "is not a valid vertex")
        row = self._mat[vi]
        i = 0
        while i < len(row):
            if row[i][0] == vj:  # 修改mat[vi][vj]的值
                self._mat[vi][vj] = (vj, val)
                return
            if row[i][0] > vj:  # 原来没有到vj的边，退出循环后加入边
                break
            i += 1
        self._mat[vi],insert(i, (vj, val))
        
    def get_edge(self, vi, vj):
        if self._invalid(vi) or self._invalid(vj):
            raise GraphError(str(vi) + 'or' + str(vj) + "is not a valid vertex")
        for i, val in self._mat[vi]:
            if i == vj:
                return val
        return self._unconn
        
    def out_edges(self, vi):
        if self._invalid(vi):
            raise GraphError(str(vi) + "is not a valid vertex")
        return self._mat[vi]

if __name__ == '__main__':
    mat = [[0,0,1], [1,0,1], [0,1,0]]
    g = Graph(mat)
    print(str(g))
    print(g.out_edges(1))
