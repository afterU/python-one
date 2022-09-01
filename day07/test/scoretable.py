'''
学生考试成绩表
'''

def main():
    names = ['关羽', '张飞', '赵云', '马超', '黄忠']
    subjs = ['语文','数学','英语']
    score = [[0]*3] * 5
    for row, name in enumerate(names):
        score[row] = [None] * 3
        print('请输入%s的成绩：' % name)
        for col, sub in enumerate(subjs):
            score[row][col] = float(input(sub + ': '))
    print(score)



if __name__ == '__main__':
    main()