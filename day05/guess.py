'''
猜数字游戏
计算机出一个1~100之间的随机数由人来猜
计算机根据人猜的数字分别给出提示大一点/小一点/猜对了
'''

import random

answer = random.randint(1, 100)
counter = 0

while True:
    counter += 1
    number = int(input("猜一猜？"))
    if number < answer:
        print("小了")
    elif number > answer:
        print("大了")
    else:
        print("恭喜您，猜对了")
        break
print('你总共猜了%d次' % counter)
if counter > 7:
    print("你的智商余额明显不够")