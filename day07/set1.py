'''
定义和使用集合
'''

def main():
    set1 = {1,2,3,3,3,2}
    print(set1)
    print(len(set1))
    set2 = set(range(1,10))
    print(set2)
    set1.add(4)
    set1.add(5)
    set2.update([11,12])
    print(set1)
    print(set2)
    set2.discard(5)
    print(set2)
    # remove的元素不存在会引发KeyError
    if 4 in set2:
        set2.remove(4)
    print(set2)

    for e in set2:
        print(e ** 2, end=' ')
    print()
    # 元素转换为set集合
    set3 = set((1,2,3,3,2,1))
    print(set3.pop())
    print(set3)


if __name__ == '__main__':
    main()