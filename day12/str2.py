from io import StringIO

def reverse_str1(str):
    return str[::-1]

def reverse_str2(str):
    if len(str) <= 1:
        return str
    return reverse_str2(str[1:]) + str[0:1]

def reverse_str3(str):
    # StringIO 对象是python中的可变字符串
    # 不应该使用不变字符串做字符串链接操作， 应为会产生很多无用字符串对象
    rstr = StringIO
    str_len = len(str)
    for i in range(str_len - 1, -1, -1):
        rstr.write(str[i])
    return rstr.getvalue()


def reverse_str4(str):
    return ''.join(str[index] for index in range(len(str) - 1, -1, -1))

def reverse_str5(str):
    str_list = list(str)
    str_len = len(str)
    # 使用zip函数将两个序列合并成一个产生元组的迭代器
    # 每次正好可以取到一前一后两个下标来实现元素的交换
    for i,j in zip(range(str_len // 2), range(str_len - 1, str_len // 2, -1)):
        str_list[i], str_list[j] = str_list[j], str_list[i]
    return ''.join(str_list)


if __name__ == '__main__':
    str_len = len('2121212')
    for i in range(str_len // 2):
        print(i, end=' ')
    print()
    for j in range(str_len - 1, str_len // 2, -1):
        print(j , end=' ')

    print(range(str_len // 2))
    print(range(str_len - 1, str_len // 2, -1))

    str = 'I love Python'
    print(str)
    print(reverse_str1(str))
    print(reverse_str2(str))
    # print(reverse_str3(str))
    print(reverse_str4(str))
    print(reverse_str5(str))
    print(str)




