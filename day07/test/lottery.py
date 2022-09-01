'''
双色球随机选好程序
'''

from random import randrange , randint, sample

def random_select():
    ''' 随机选择一组号码'''
    red_balls = [x for x in range(1, 34)]
    selected_balls = []
    for _ in range(6):
        index = randrange(len(red_balls))
        selected_balls.append(red_balls[index])
        del red_balls[index]
    # 从red_balls中随机选择6个不重复的号码 等同于一下一行代码
    # selected_balls = sample(red_balls, 6)
    selected_balls.sort()
    selected_balls.append(randint(1, 16))
    return selected_balls

def format_show(select_balls):
    for i,item in enumerate(select_balls):
        if i == len(select_balls) - 1:
            print('|', end=' ')
        print(select_balls[i], end=' ')
    print()

def main():
    n = int(input('机选几注：'))
    for _ in range(n):
        format_show(random_select())

if __name__ == '__main__':
    main()