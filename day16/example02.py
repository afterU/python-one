'''
排序 -- 冒泡排序， 选择排序， 快速排序， 归并排序

-------------------------------------------
冒泡排序 - O(n ** 2) 两两比较， 大的下沉
-------------------------------------------
选择排序 O(n ** 2) 每次从剩下元素中选择最小的
-------------------------------------------
快速排序 以轴为届将列表中的元素划分为两个部分， 左边都比枢轴小，右边都比枢轴大
-------------------------------------------
归并排序 O(n * log_2 n)
'''

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = name

    def __str__(self):
        return f'{self.name}:{self.age}'

    def __repr__(self):
        return self.__str__()

'''
选择排序
'''
def select_sort(origin_items, comp=lambda x,y:x<y):
    items = origin_items[:]
    for i in range(len(items)-1):
        min_index = i
        for j in range(i+1,len(items)):
            if comp(items[j],items[min_index]):
                min_index = j
        items[i], items[min_index] = items[min_index], items[i]
    return items

'''
* 前面的参数叫位置参数， 传参是按照位置来就可以
* 后面的参数叫命名关键字参数，传参时必须给出参数名和参数值
*args - 可变参数 - 元组
**kwargs - 关键字参数 - 字典
'''
'''
冒泡排序
'''
def bubble_sort(origin_items, *, comp=lambda x,y: x>y):
    items = origin_items[:]
    for i in range(1,len(items)):
        swapped = False
        for j in range(i-1, len(items) - i):
            if comp(items[j], items[j+1]):
                items[j], items[j+1] = items[j-1], items[j]



