import json
import csv2


json_str = '{"name": "骆昊", "age": 38, "title": "叫兽"}'
result = json.loads(json_str)
print(type(result))
print(result)
print(result['name'])
print(result['age'])


# 把json反序列化出来的dict作为参数传入Teacher的构造器
# * 组装和拆解元组作为函数参数， ** 组装和拆解字典作为函数参数
teacher = csv2.Teacher(**result)
print(teacher)
print(teacher.name)
print(teacher.age)
print(teacher.title)