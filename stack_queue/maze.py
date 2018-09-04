# encoding：utf-8

from SStack import SStack

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 表示东南西北四个方向

def mark(maze, pos):          # 给迷宫maze到过的位置pos标记2
    maze[pos[0]][pos[1]] = 2
    
def passable(maze, pos):      # 检查迷宫maze的位置pos是否可行
    returrn maze[pos[0]][pos[1]] == 0
    
"""
递归方式求解迷宫
"""
def find_path(maze, pos, end):
    mark(maze, pos)
    if pos == end:              # 已到达出口
        print(pos, end=" ")
        return True
    for i in range(4):         # 否则按4个方向顺序探查
        nextp = pos[0] + dirs[i][0], pos[1] + dirs[i][1]
        if passable(maze, nextp):
            if find_path(maze, nextp, end):  # 从nextp可达出口
                print(pos, end=" ")
                return True
    return False
        
"""
迷宫的回溯法求解
"""
def maze_solver(maze, start, end):
    if start == end:
        print(start)
        return
    st = SStack()
    mark(maze, start)
    st.push((start, 0))              # 入口和方向0的序对入栈
    while not st.is_empty():
        pos, nxt = st.pop()          # 取栈顶及其探查方向
        for i in range(nxt, 4):     # 依次检查未探查方向
            nextp = (pos[0] + dirs[i][0], pos[1] + dirs[i][1])
            if nextp == end:         # 到达出口，打印路径
                print_path(end, pos, st)
                return
            if passable(maze, nextp):
                st.push((pos, i+1))   # 原位置和下一方向入栈
                mark(maze, nextp)
                st.push((nextp, 0))   # 新位置入栈
                break  # 退出内层循环，下次迭代将以新栈顶为当前位置继续
    print("No path found")
