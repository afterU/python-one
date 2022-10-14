import itertools
import operator

'''count(a,b), 从a开始，步距为b'''
for i in itertools.count(1,2):
    print(i)
    if i > 10:
        break
''' islice(a,b) 从a开始，获取b个元素'''
for i in itertools.islice(itertools.count(10), 5):
    print(i)

'''cycle(a) a可以是元素，字符串，列表 在a范围内反复循环'''
count = 0
for item in itertools.cycle('xyz'):
    if count > 7:
        break
    print(item)
    count += 1

'''itertools.accumulate(a,b) a可迭代对象，操作函数。 迭代器返回可迭代对象累计操作的结果 '''
l = list(itertools.accumulate(range(1, 6), operator.mul))
print(l)

'''itertools.chain() 将多个可迭代对象合并为一个'''
for i in itertools.chain(['q','a','b'], ['ee',123],'xyz'):
    print(i)
''' itertools.groupby() 将迭代器中相邻的重复的元素挑出来放在一起'''
for key, group in itertools.groupby('aaaabbbcccdddda'):
    print(key,list(group))
