def main():
    str1 = 'hello, world!'
    # 通过len函数计算字符串的长度
    print(len(str1))
    # 生成字符串的首字母大写
    print(str1.capitalize())
    # 生成字符串的大写
    print(str1.upper())
    # 查找子字符串中查找子串的位置
    print(str1.find('or'))
    print(str1.find('shit')) # 找不到返回-1
    # 与find类似， 找不到会跑出异常
    print(str1.index('or'))
    # print(str1.index('shit'))
    # 检查字符串是否以指定的子串结尾
    print(str1.endswith('!'))
    # 检查字符串是否以指定的子串开始
    print(str1.startswith('hel'))
    print(str1.startswith('He'))
    # 将字符串以指定的宽度剧中并在两侧填充指定的字符
    print(str1.center(50,'*'))
    # 将字符串以指定的宽度靠右放置左侧填充指定的字符
    print(str1.rjust(50,'*'))
    str2 = 'abc123456'
    # 从字符串中取出指定位置的字符
    print(str2[2])
    # 字符串切片（从指定的开始索引0到指定的结束索引）
    print(str2[2:5])
    print(str2[2:])
    # 从0开始每个2位 ac246
    print(str2[::2])
    # 从1开始每个5位
    print(str2[1::5])
    # 每隔-1实现字符串反转
    print(str2[::-1])

    print(str2[-3:-1])

    # 检查字符串是否都是数字组成
    print(str2.isdigit())
    # 检查字符串是否都是字母组成
    print(str2.isalpha())
    # 检查字符串是否以数字和字母组成
    print(str2.isalnum())

    # 修剪字符串两侧的空格
    print('   hello   '.strip())
    # 修剪字符串两侧的特殊字符
    print('$$hello world$'.strip('$'))


if __name__ == '__main__':
    main()