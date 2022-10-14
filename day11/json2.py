'''
json写入文件
'''
import json

teacher_dict = {'name': '白元芳','age':24, 'title':'将使'}

json_str = json.dumps(teacher_dict)
print(json_str)
print(type(json_str))
fruits = ['apple','banana','orange','pitaya','strawberry']
json_str = json.dumps(fruits)
print(json_str)
print(type(json_str))