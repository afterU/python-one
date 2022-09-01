'''
元组的定义和使用
'''
def main():
    # 定义元组
    t = ('张三', 33, True, '澳大利亚')
    print(t)
    print(t[0])
    print(t[1])
    print(t[2])
    print(t[3])
    # 会产生角标越界
    # print(t[4])

    for e in t:
        print(e)
    # 重新给元组赋值， 会报错
    # t[0] = '王大锤'
    t = ('王大锤', 22, False, '美国')
    print(t)

    # list 和 元组 互转
    person = list(t)
    print(person)
    person[0] = '李小龙'
    person[1] = 50
    print(person)

    fruits_list = ['apple', 'banana', 'orange']
    fruits_tuple = tuple(fruits_list)
    print(fruits_tuple)
    print(fruits_tuple[1])
if __name__ == '__main__':
    main()