# encoding:utf-8

# 冒泡排序

def bubble_sort(lst):
    for i in range(len(lst)):
        found = False
        for j in range(1, len(lst)-i):
            if lst[j-1] > lst[j]:
                lst[j-1], lst[j] = lst[j], lst[j-1]
                found = True
        if not found:  # 没有发生交换
            break
            
if __name__ == '__main__':
    lst = [1, 6, 5, 44, 7, 5, 81, 2]
    bubble_sort(lst)
    print(lst)
