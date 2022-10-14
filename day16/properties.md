## python的特殊用法
1. 生成式(推导式)语法, 生成器
   - 可以用于生成列表，集合，字典
     - 列表生成式
        ```
         nums = [num for num in range(1,101) if num %3 == 0]
        ```
     - 集合生成式
       ```
       result = {i ** 2 for i in range(10)}
       ```
     - 字典生成式
       ```
       result = {i:i**2 for i in range(10)}
       ```
   - 生成器
     - 一边循环一边计算的机制，成为生成器 generator。 面对大文件的时候，可以节省内存。
       ```
        nums = [i ** 2 for i in range(100000)]
       # 当计算次数比较多的时候，电脑的资源占用比较严重， 计算有一定的时间， 仅仅需要知道前几个的数值此时可以使用生成器
       nums = [i ** 2 for i in range(100000)]
       print(next(nums))
        ```
     - 生成器的第二种写法 yield关键字
       ```
       # return : 函数遇见return就返回， return后面的代码并不会执行
       # yield ： 函数遇见yield则停止执行代码，当再次调用next方法时， 会从上次停止的地方继续执行， 遇见yield停止
        def login():
            print('step 1')
            yield 1
            print('step 2')
            yield 2
            print('step 3')
            yield 3
        ``` 
2. heapq itertools collections等的用法
   - heapq 获取最大，最小的元素
     ```
      import  heapq
      list1 = [34, 25, 12, 99, 87, 63, 58, 78, 88, 92]
      print(heapq.nlargest(3, list1))
      print(heapq.nlargest(1, list1))
      list2 = [
        {'name': 'IBM', 'shares': 100, 'price': 91.1},
        {'name': 'AAPL', 'shares': 50, 'price': 543.22},
        {'name': 'FB', 'shares': 200, 'price': 21.09},
        {'name': 'HPQ', 'shares': 35, 'price': 31.75},
        {'name': 'YHOO', 'shares': 45, 'price': 16.35},
        {'name': 'ACME', 'shares': 75, 'price': 115.65}
      ]
      print(heapq.nlargest(2, list2, key=lambda x:x['price']))
     ```
   - itertools 迭代器工具包
     ```
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
      ```
   - collections模块下的工具类
     - collections模块在内置数据类型（dict、list、set、tuple）的基础上， 还提供了几个额外的数据类型：ChainMap、Counter、deque、defaultdict、namedtuple和OrderedDict等。
        1. defaultdict: 带有默认值的字典
        2. OrderedDict: 有序字典
        3. Counter: 计数器，主要用来计数
        4. deque: 双端队列，可以快速的从另外一侧追加和推出对象
        5. namedtuple: 生成可以使用名字来访问元素内容的tuple子类
3. * 组装和拆解元组作为函数参数， ** 组装和拆解字典作为函数参数

4. 函数的使用方式
   - 将函数视为“一等公民”
     - 函数可以赋值给变量
     - 函数可以作为函数的参数
     - 函数可以作为函数的返回值
     - 高阶函数的用法（`filter`、`map`以及它们的替代品）
       ```Python
       items1 = list(map(lambda x: x ** 2, filter(lambda x: x % 2, range(1, 10))))
       items2 = [x ** 2 for x in range(1, 10) if x % 2]
       ```
     - 位置参数、可变参数、关键字参数、命名关键字参数
        # *前面的参数叫位置参数，传参时只需要对号入座即可
        # *后面的参数叫命名关键字参数，传参时必须给出参数名和参数值
        # *args - 可变参数 - 元组
        # **kwargs - 关键字参数 - 字典
     - 参数的元信息（代码可读性问题）

     - 匿名函数和内联函数的用法（`lambda`函数）
        - 当一些函数很简单，仅仅只是计算一个表达式的值的时候，就可以使用lambda表达式来代替了
     - 闭包和作用域问题

       - Python搜索变量的LEGB顺序（Local --> Embedded --> Global --> Built-in）

       - `global`和`nonlocal`关键字的作用

         `global`：声明或定义全局变量（要么直接使用现有的全局作用域的变量，要么定义一个变量放到全局作用域）。

         `nonlocal`：声明使用嵌套作用域的变量（嵌套作用域必须存在该变量，否则报错）。

     - 装饰器函数（使用装饰器和取消装饰器）
