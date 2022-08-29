'''
定义和使用字典
'''

def main():
    score = {'螺号':95,'远方':78,'狄仁杰':82}
    print(score['螺号'])
    print(score['狄仁杰'])
    for e in score:
        print('%s\t---->\t%d' % (e, score[e]))
    score['螺号'] = 99
    score["张三"] = 77
    print(score)
    if '武则天' in score:
        print(score['武则天'])
    print(score.get('武则天'))
    print(score.get('武则天', 80))
    print(score.popitem())
    print(score.popitem())
    print(score.pop('螺号', 1000))
    score.clear()
    print(score)

def main2():
    stu = {'name':'螺号', 'age':38, 'gender': True}
    print(stu)
    print(stu.keys())
    print(stu.values())
    print(stu.items())
    for i in stu.items():
        print(i)
        print(i[0],i[1])
    if 'age' in stu:
        stu['age'] = 20
    print(stu)
    stu.setdefault('score', 60)
    print(stu)
    stu.setdefault('score', 100)
    print(stu)
    stu['score'] = 100
    print(stu)


if __name__ == '__main__':
    # main()
    main2()