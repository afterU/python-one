'''
列表常用操作
- 列表链接
- 列表长度
- 遍历列表
- 列表切片
- 列表排序
- 列表反转
- 查找元素
'''

def main():
    fruits = ['grape', 'apple', 'strawberry', 'waxberry']
    fruits += ['pitaya', 'pear', 'mango']
    # 遍历列表
    for fruit in fruits:
        print(fruit.title(), end='')
    print()

    # 列表切片
    fruits2 = fruits[1:4]
    print(fruits2)
    # 没有复制列表只创建了新的引用
    fruits3 = fruits
    fruits4 = fruits[:]
    print(fruits4)
    fruits5 = fruits[-3:-1]
    print(fruits5)
    # 列表反转
    fruits6 = fruits[::-1]
    print(fruits6)

if __name__ == '__main__':
    main()