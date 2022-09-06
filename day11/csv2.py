'''
写入csv文件
'''

import csv

class Teacher(object):
    def __init__(self, name, age, title):
        self._name = name
        self._age = age
        self._title = title
        self._index = -1

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @property
    def title(self):
        return self._title

filename = 'teacher.csv'
teachers = [Teacher('张三', 20, '教授'), Teacher('李四', 50, '专家')]

try:
    with open(filename, 'w') as f:
        writer = csv.writer(f)
        for t in teachers:
            writer.writerow([t.name,t.age,t.title])
except BaseException as e:
    print('无法写入文件', filename)
else:
    print('保存数据成功')