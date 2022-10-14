import re

def main():
    pattern = re.compile(r'(?<=\D)(1[38]\d{9}|14[57]\d{8}|15[0-35-9]\d{8}|17[678]\d{8})(?=\D)')
    source = '''重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，
    不是15600998765，也是110或119，王大锤的手机号才是15600998765。'''

    # 查找匹配的字符串放到list中
    list = re.findall(pattern, source)
    print(list)

    for iterm in re.finditer(pattern, source):
        print(iterm.group())

    # source函数指定位置进行匹配
    m = pattern.search(source)
    while m:
        print(m.group())
        m = pattern.search(source, m.end())


if __name__ == '__main__':
    main()

