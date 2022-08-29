'''
定义和使用列表
'''

def main():
    fruits = ['grape', 'apple', 'strawberry', 'waxberry']
    print(fruits)

    # 通过下标访问
    print(fruits[0])
    print(fruits[1])
    print(fruits[2])
    print(fruits[-1])
    print(fruits[-2])

    fruits[1] = 'apple2'
    print(fruits)

    # 添加元素
    print('---------------------------')

    fruits.append('pitaya')
    fruits.insert(0, 'banana')
    fruits.insert(0, 'banana')
    print(fruits)

    # 删除
    print('---------------------------')
    fruits.remove('banana')
    print(fruits)
    del fruits[1]
    print(fruits)
    fruits.pop()
    print(fruits)
    fruits.pop(1)
    print(fruits)




if __name__ == '__main__':
    main()
