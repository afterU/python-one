'''
输入学生的考试成绩计算平均分
'''

def main():
    number = int(input('请输入学生人数：'))
    # 初始化number个数的list
    names = [None] * number
    scores = [None] * number
    for i in range(len(names)):
        names[i] = input('请输入第%d个学生的名字：' % (i + 1))
        scores[i] = float(input('请输入第%d个学生的成绩：' % (i + 1)))
    total = 0
    for i in range(len(names)):
        print('%s : %.1f分' % (names[i], scores[i]))
        total += scores[i]
        print(type((total / number)))
    print('平均成绩是: %.1f分' % (total / number))
    print(names)
    print(type(names))
    pass

if __name__ == '__main__':
    main()