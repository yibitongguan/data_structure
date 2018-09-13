# encoding:utf-8

# 插入排序
def insert_sort(lst):
    for i in range(1, len(lst)):  # 开始时第一个元素已排序
        x = lst[i]
        j = i
        while j > 0 and lst[j-1] > x:
            lst[j] = lst[j-1]       # 元素后移
            j -= 1
        lst[j] = x

if __name__ == '__main__':
    lst = [1, 6, 5, 44, 7, 5, 81, 2]
    insert_sort(lst)
    print(lst)
