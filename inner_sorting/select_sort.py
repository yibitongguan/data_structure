# encoding:utf-8

# 直接选择排序
def select_sort(lst):
    for i in range(len(lst)-1):
        k = i
        for j in range(i, len(lst)):  # 求得k是最小元素的位置
            if lst[j] < lst[k]:
                k = j
        if i != k:
            lst[i], lst[k] = lst[k], lst[i]
            
if __name__ == '__main__':
    lst = [1, 6, 5, 44, 7, 5, 81, 2]
    select_sort(lst)
    print(lst)
            
