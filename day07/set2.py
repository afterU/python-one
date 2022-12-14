'''
集合中常用操作
- 交集
- 并集
- 差集
- 子集
- 超集
'''

def main():
    set1 = set(range(1,7))
    print(set1)
    # 最后一个参数代表步距
    set2 = set(range(2, 11, 2))
    print(set2)
    set3 = set(range(1, 5))
    # 交集
    print(set1 & set2)
    print(set1.intersection(set2))
    # 并集
    print(set1 | set2)
    print(set1.union(set2))
    # 差集
    print(set1.difference(set2))
    print(set1 - set2)

    # 补集
    print(set1.symmetric_difference(set2))
    print(set1 ^ set2)

    # 子集
    print(set2.issubset(set1))
    print(set2 <= set1)

    print(set3 <= set1)
    print(set3.issubset(set1))

    # 父集
    print(set1.issuperset(set2))
    print(set1 >= set2)

    print(set1.issuperset(set3))
    print(set1 >= set3)


    pass
if __name__ == '__main__':
    main()