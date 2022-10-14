'''
查找-- 顺序查找 和 二分查找
'''
import getpass
import os
from math import log2, factorial
from matplotlib import pyplot

import numpy

def seq_search(items: list, elem) -> int:
    for index , item in enumerate(items):
        if elem == item:
            return index
    return -1

def bin_search(items, elem):
    start, end = 0, len(items) - 1
    while start <= end:
        mid = (start + end) // 2
        if elem > items[mid]:
            start = mid + 1
        elif elem < items[mid]:
            end = mid - 1
        else:
            return mid
    return -1

def main():
    num = 6
    styles = ['r-.','g-*','b-o','y-x','c-^','m-+','k-d']
    legends = ['对数','线性','线性代数','平方','立方','几何级数','阶乘']
    x_data = [x for x in range(1, num + 1)]
    y_data1 = [log2(y) for y in range(1, num+1)]
    y_data2 = [y for y in range(1, num+1)]
    y_data3 = [y * log2(y) for y in range(1, num+1)]
    y_data4 = [y ** 2 for y in range(1, num +1)]
    y_data5 = [y ** 3 for y in range(1, num+1)]
    y_data6 = [3 ** y for y in range(1, num+1)]
    y_data7 = [factorial(y) for y in range(1, num +1)]
    y_datas = [y_data1,y_data2,y_data3,y_data4,y_data5,y_data6,y_data7]
    for index, y_data in enumerate(y_datas):
        pyplot.plot(x_data, y_data, styles[index])
    pyplot.legend(legends)
    pyplot.xticks(numpy.arange(1,7,step=1))
    pyplot.yticks(numpy.arange(0, 751, step=50))
    pyplot.show()

if __name__ == '__main__':
    # dir(os)
    help(os)
    # main()


